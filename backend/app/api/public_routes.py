from flask import Blueprint, request, jsonify, current_app
from .mail import send_verification_email, send_reset_password_email
from werkzeug.security import generate_password_hash
import jwt
from os import getenv, urandom
from db import my_db
from datetime import datetime, timedelta

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
USE_FLASK_LIMITER = getenv("USE_FLASK_LIMITER").lower() == "true"

public_blueprint = Blueprint('verification', __name__)

if USE_FLASK_LIMITER:
    limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])
    limiter.init_app(public_blueprint)


@public_blueprint.route('/send_verification_email', methods=['POST'])
def resend_verification_email():
    data = request.json
    email = data.get('email')
    if not email:
        return jsonify({'error': 'Email address is required.'}), 400

    user_id = my_db.get_user_id_from_identifier(email)
    if user_id is None:
        return jsonify({'error': 'Email not found.'}), 404

    if my_db.is_user_verified(user_id):
        return jsonify({'message': 'Email already verified.'}), 200

    # Resend verification email logic
    exp = datetime.utcnow() + timedelta(hours=24)
    token = jwt.encode({'user_id': user_id, 'exp': exp},
                       getenv('JWT_SECRET_KEY'), algorithm='HS256')
    send_verification_email(email, token)
    return jsonify({'message': 'Verification email resent.'}), 200

@public_blueprint.route('/verify', methods=['GET'])
def verify_email():
    token = request.args.get('token')
    if not token:
        return jsonify({'error': 'No token provided'}), 400

    try:
        # Decode the token
        decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        user_id = decoded.get('user_id')
        # Check expiration internally handled by jwt.decode

        # Set the user as verified
        my_db.mark_user_as_verified(user_id)
        return jsonify({'message': 'Email successfully verified'}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 400
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400

@public_blueprint.route('/reset_password', methods=['GET'])
def verify_reset_password():
    token = request.args.get('token')
    if not token:
        return jsonify({'error': 'No token provided'}), 400
    
    try:
        decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        user_id = decoded.get('user_id')

        # Get and encrypt the new password
        raw_new_password = decoded.get('new_password')
        salt = urandom(16).hex()
        hashed_password = generate_password_hash(raw_new_password + salt)
        my_db.update_password(user_id, hashed_password, salt)
        message = 'Your password has been reset successfully.'

        return jsonify({'message': message}), 201
    
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 400
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400