from flask import request, jsonify, g, current_app
import jwt
from functools import wraps
from os import getenv
secret_key = getenv("JWT_SECRET_KEY")
USE_HTTP_COOKIES = getenv("USE_HTTP_COOKIES").lower() == "true"

def get_token():
    if USE_HTTP_COOKIES:
        return request.cookies.get('token')
    else:
        auth_header = request.headers.get('Authorization')
        return auth_header.split(" ")[1] if auth_header and auth_header.startswith('Bearer ') else None


def get_user_id_from_token():
    token = get_token()
    try:
        decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded.get('user_id')
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = get_token()
        if not token:
            return jsonify({'message': 'Authentication required'}), 403

        # Retrieve the user ID from the cache
        cache_key = f"token_{token}"
        user_id_from_token = current_app.cache.get(cache_key)

        if user_id_from_token is None:
            try:
                payload = jwt.decode(token, secret_key, algorithms=['HS256'])
                user_id_from_token = payload['user_id']
                current_app.cache.set(cache_key, user_id_from_token, timeout=300)  # Cache for 5 minutes
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 403
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 403

        g.user_id_from_token = user_id_from_token
        return f(*args, **kwargs)

    return decorated_function

def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = get_token()
        if token:
            try:
                jwt.decode(token, secret_key, algorithms=['HS256'])
                # If this point is reached, the user is authenticated
                return jsonify({'message': 'You are already logged in'}), 403
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                # Token is invalid or expired, allow the request
                pass
        return f(*args, **kwargs)
    return decorated_function