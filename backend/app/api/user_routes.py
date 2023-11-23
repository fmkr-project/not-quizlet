from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from os import urandom
from .auth import login_required
from db import my_db
import jwt
import datetime
from os import getenv

JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    client_hashed_password = data.get('password')  # Already hashed by client
    if not username or not email or not client_hashed_password:
        return jsonify({'error': 'Missing fields'}), 400

    if my_db.user_exists_already(username=username, email=email):
        return jsonify({'error': 'Username or Email already registered'}), 409
    salt = urandom(16).hex()
    server_hash = generate_password_hash(client_hashed_password + salt)
    if my_db.register_user(username, email, server_hash, salt):
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'error': 'Registration failed'}), 500

@user_blueprint.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')  
    client_hashed_password = data.get('password')  # Already hashed by client
    if not email or not client_hashed_password:
        return jsonify({'error': 'Missing fields'}), 400   
    user = my_db.login_user(email, client_hashed_password)
    if user:
        token = jwt.encode({
            'user_id': user['id'],  
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, JWT_SECRET_KEY, algorithm='HS256')

        return jsonify({'token': token.decode('UTF-8')}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
@login_required
def get_user_details(user_id, user_id_from_token):
    # Compare user_id from the route with the user_id in the token
    if user_id != user_id_from_token:
        return jsonify({'message': 'Unauthorized'}), 403
    else:
        user_details = my_db.get_user_details(user_id)
        if user_details:
            # Optionally, convert the result to a dict or similar structure as needed
            return jsonify({'user': user_details}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

