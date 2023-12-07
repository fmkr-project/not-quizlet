from flask import Blueprint
from flask_cors import CORS
from .user_routes import user_blueprint
from .deck_routes import deck_blueprint
from .card_routes import card_blueprint
from .test_routes import test_blueprint
from .public_routes import public_blueprint
from .database_routes import database_blueprint
from os import getenv
from .mail import send_verification_email
API_VERSION = getenv("API_VERSION")

api_blueprint = Blueprint(API_VERSION, __name__)

private_api_blueprint = Blueprint('private_api', __name__, url_prefix='/api')
public_api_blueprint = Blueprint('public_api', __name__)

private_api_blueprint.register_blueprint(user_blueprint, url_prefix='/users')
private_api_blueprint.register_blueprint(deck_blueprint, url_prefix='/decks')
private_api_blueprint.register_blueprint(card_blueprint, url_prefix='/cards')
private_api_blueprint.register_blueprint(test_blueprint, url_prefix='/tests')
private_api_blueprint.register_blueprint(database_blueprint, url_prefix='/db')

public_api_blueprint.register_blueprint(public_blueprint)

api_blueprint.register_blueprint(public_api_blueprint)
api_blueprint.register_blueprint(private_api_blueprint)

CORS(api_blueprint, supports_credentials=True, origins="http://localhost:8080")