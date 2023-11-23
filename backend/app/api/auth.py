from flask import request, jsonify
import jwt
from functools import wraps
from os import getenv
secret_key = getenv("JWT_SECRET_KEY")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            # Use the secret_key from your environment variables
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(*args, **kwargs, user_id=payload['user_id'])
    return decorated_function