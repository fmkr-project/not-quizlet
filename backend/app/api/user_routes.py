from flask import Blueprint, request, jsonify, g, current_app, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from os import urandom
from .auth import login_required, logout_required, get_user_id_from_token, get_token
from db import my_db
from .mail import send_verification_email, send_reset_password_email
import jwt
from datetime import datetime, timedelta
from dateutil import parser
from os import getenv
import logging
logging.basicConfig(level=logging.DEBUG)

USE_MAIL_VERIFICATION = getenv('USE_MAIL_VERIFICATION').lower() == 'true'
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")

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
            # Generate and send verification token
            exp = datetime.utcnow() + timedelta(hours=24)
            token = jwt.encode({'user_id': user_id, 'exp': exp},
                               getenv('JWT_SECRET_KEY'), algorithm='HS256')
            send_verification_email(email, token)
            message = 'User registered successfully. Please check your email to verify your account.'
        else:
            # Auto-verify user in the database
            my_db.mark_user_as_verified(user_id)  
            message = 'User registered successfully.'

        return jsonify({'message': message}), 201
    except Exception as e:
        logging.exception("Registration failed: %s", e)
        return jsonify({'error': 'Registration failed', 'details': str(e)}), 500

@user_blueprint.route('/login', methods=['POST'])
@logout_required
def login_user():
    data = request.json
    email = data.get('email')  
    client_hashed_password = data.get('password')  # Already hashed by client
    remember_me = data.get('rememberMe', False)
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
    if failed_attempts and failed_attempts['attempts'] >= 3:
        last_failed_login = failed_attempts['last_failed_login']
        time_since_last_fail = datetime.utcnow() - parser.parse(last_failed_login)
        delay = min(2 ** (failed_attempts['attempts'] - 3), 120)
        if time_since_last_fail.total_seconds() < delay:
            return jsonify({'error': f'Too many failed attempts from this IP. Try again in {delay} seconds.'}), 429

    user = my_db.login_user(email, client_hashed_password)
    if USE_MAIL_VERIFICATION and user and not my_db.is_user_verified(user_id):
        return jsonify({'error': 'Please check your email and verify your account using the verification link.'}), 401
    if user:
        my_db.reset_failed_attempts(user_id, client_ip)  # Reset on successful login
        token = jwt.encode({
            'user_id': user_id,  
            'exp': datetime.utcnow() + timedelta(days=365)
        }, JWT_SECRET_KEY, algorithm='HS256')
        response = make_response(jsonify({'success': True, 'message': 'Login successful'}), 201)
        if remember_me:
            token = jwt.encode({
                'user_id': user_id,  
                'exp': datetime.utcnow() + timedelta(days=365)
            }, JWT_SECRET_KEY, algorithm='HS256')
            response.set_cookie('token', token, httponly=True, expires=datetime.utcnow() + timedelta(days=365))
        else:
            token = jwt.encode({
                'user_id': user_id,  
                'exp': datetime.utcnow() + timedelta(days=7)
            }, JWT_SECRET_KEY, algorithm='HS256')            
            response.set_cookie('token', token, httponly=True)
        return response
    else:
        my_db.increment_failed_attempts(user_id, client_ip)  # Log failed attempt
        return jsonify({'error': 'Invalid credentials'}), 401


@user_blueprint.route('/get_details/<int:user_id>/<int:privacy>', methods=['GET'])
@login_required
def get_user_details(user_id, privacy):
    user_id_from_token = getattr(g, 'user_id_from_token', None)
    if user_id_from_token is None:
        return jsonify({'error': 'Unauthorized'}), 403

    if user_id != user_id_from_token:
        return jsonify({'message': 'Unauthorized'}), 403
    else:
        cache_key = f"user_details_{user_id}_{privacy}"
        user_details = current_app.cache.get(cache_key)

        if user_details is None:
            user_details = my_db.get_user_details(user_id, privacy)
            if user_details:
                current_app.cache.set(cache_key, user_details, timeout=300)  # Cache for 5 minutes
            else:
                return jsonify({'error': 'User not found'}), 404

        return jsonify({'user': user_details}), 200


@user_blueprint.route('/send_reset_password', methods=['POST'])
@logout_required
def send_reset_password():
    data = request.json
    email = data.get('email')
    new_password = data.get('password')
    user_id = my_db.get_user_id_from_identifier(email)
    token = jwt.encode({
            'user_id': user_id,
            'new_password': new_password,
            'exp': datetime.utcnow() + timedelta(days=365)
        }, JWT_SECRET_KEY, algorithm='HS256')
    if user_id:
        send_reset_password_email(email, token)
        return jsonify({'message': 'Successful'}), 201
    else:
        return jsonify({'error': 'User not found'}), 404
    
@user_blueprint.route('/logout', methods=['POST'])
@login_required
def logout_user():
    user_id_from_token = getattr(g, 'user_id_from_token', None)
    if user_id_from_token:
        token = request.cookies.get('token')
        if token:
            cache_key = f"token_{token}"
            current_app.cache.delete(cache_key)
        response = make_response(jsonify({'message': 'Logged out successfully'}))
        response.set_cookie('token', '', expires=0, httponly=True)
        return response
    else:
        return jsonify({'error': 'Not logged in'}), 400
    
@user_blueprint.route('/check_auth', methods=['GET'])
@login_required
def check_auth():
    return jsonify({'message': 'User is authenticated'}), 200