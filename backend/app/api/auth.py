from flask import request, jsonify, g
import jwt
from functools import wraps
from os import getenv
secret_key = getenv("JWT_SECRET_KEY")

def get_user_id_from_token():
    token = request.headers.get('Authorization').split(" ")[1]
    try:
        decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded.get('user_id')
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Extract token from the Authorization header
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(" ")[1]
        else:
            return jsonify({'message': 'Bearer token not provided or malformed'}), 403

        try:
            # Decode the token using the secret key
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            g.user_id_from_token = payload['user_id']  # Store in Flask's global context
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(*args, **kwargs)

    return decorated_function

def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
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