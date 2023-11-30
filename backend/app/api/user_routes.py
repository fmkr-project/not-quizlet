from flask import Blueprint, request, jsonify, g, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from os import urandom
from .auth import login_required, logout_required
from db import my_db
from .mail import send_verification_email
import jwt
from datetime import datetime, timedelta
from dateutil import parser
from os import getenv

USE_MAIL_VERIFICATION = getenv('USE_MAIL_VERIFICATION').lower == 'true'
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")

def get_user_id_from_token():
    token = request.headers.get('Authorization').split(" ")[1]
    try:
        decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        return decoded.get('user_id')
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return None


user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/register', methods=['POST'])
@logout_required
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    client_hashed_password = data.get('password')  # Already hashed by client

    if not username or not email or not client_hashed_password:
        return jsonify({'error': 'Missing fields'}), 400

    if my_db.user_exists_already(username=username, email=email)['any']:
        return jsonify({'error': 'Username or Email already registered'}), 409

    salt = urandom(16).hex()
    server_hash = generate_password_hash(client_hashed_password + salt)

    try:
        user_id = my_db.register_user(username, email, server_hash, salt)
        user_id = my_db.get_user_id_from_identifier(email)
        if USE_MAIL_VERIFICATION:
            # Generate, store, and send verification token
            exp = datetime.utcnow() + timedelta(hours=24)
            token = jwt.encode({'user_id': user_id, 'exp': exp},
                               getenv('JWT_SECRET_KEY'), algorithm='HS256')
            my_db.store_verification_token(user_id, token, exp.isoformat())
            send_verification_email(email, token)
            message = 'User registered successfully. Please check your email to verify your account.'
        else:
            # Auto-verify user in the database
            my_db.mark_user_as_verified(user_id)  
            message = 'User registered successfully.'

        return jsonify({'message': message}), 201
    except Exception as e:
        return jsonify({'error': 'Registration failed', 'details': str(e)}), 500

@user_blueprint.route('/login', methods=['POST'])
@logout_required
def login_user():
    data = request.json
    email = data.get('email')  
    client_hashed_password = data.get('password')  # Already hashed by client
    client_ip = request.remote_addr
    if not email or not client_hashed_password:
        return jsonify({'error': 'Missing fields'}), 400

    user_id = my_db.get_user_id_from_identifier(email)
    if user_id is None:
        return jsonify({'error': 'This account is not registered.'}), 401
    # Check if the account is locked
    if my_db.is_account_locked(user_id):
        return jsonify({'error': 'Account is locked due to suspicious activity'}), 403

    # Check for failed login attempts from multiple IPs
    if my_db.has_multiple_failed_logins(user_id, hours=5, threshold=3):
        my_db.lock_account(user_id)
        return jsonify({'error': 'Account is locked due to suspicious activity'}), 403

    # Check for failed attempts and delay for the current IP
    failed_attempts = my_db.get_failed_attempts_for_ip(user_id, client_ip)
    print(failed_attempts)
    if failed_attempts and failed_attempts['attempts'] >= 3:
        last_failed_login = failed_attempts['last_failed_login']
        print(last_failed_login)
        time_since_last_fail = datetime.utcnow() - parser.parse(last_failed_login)
        print(time_since_last_fail)
        delay = min(2 ** (failed_attempts['attempts'] - 3), 120)
        if time_since_last_fail.total_seconds() < delay:
            return jsonify({'error': f'Too many failed attempts from this IP. Try again in {delay} seconds.'}), 429

    user = my_db.login_user(email, client_hashed_password)
    print(user)
    if user:
        my_db.reset_failed_attempts(user_id, client_ip)  # Reset on successful login
        token = jwt.encode({
            'user_id': user_id,  
            'exp': datetime.utcnow() + timedelta(days=365)
        }, JWT_SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token}), 200
    else:
        my_db.increment_failed_attempts(user_id, client_ip)  # Log failed attempt
        return jsonify({'error': 'Invalid credentials'}), 401


@user_blueprint.route('/get_details/<int:user_id>/<int:privacy>', methods=['GET'])
@login_required
def get_user_details(user_id, privacy):  
    user_id_from_token = getattr(g, 'user_id_from_token', None)
    if user_id_from_token is None:
        return jsonify({'error': 'Unauthorized'}), 403
    # Compare user_id from the route with the user_id in the token
    if user_id != user_id_from_token:
        return jsonify({'message': 'Unauthorized'}), 403
    else:
        user_details = my_db.get_user_details(user_id, privacy)
        if user_details:
            return jsonify({'user': user_details}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

