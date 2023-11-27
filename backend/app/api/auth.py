from flask import request, jsonify, g
import jwt
from functools import wraps
from os import getenv
secret_key = getenv("JWT_SECRET_KEY")


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