from flask import Blueprint
from .user_routes import user_blueprint
from .deck_routes import deck_blueprint
from .card_routes import card_blueprint
from .test_routes import test_blueprint
from os import getenv
API_VERSION = getenv("API_VERSION")

api_blueprint = Blueprint(API_VERSION, __name__, url_prefix='/api')
api_blueprint.register_blueprint(user_blueprint, url_prefix='/users')
api_blueprint.register_blueprint(deck_blueprint, url_prefix='/decks')
api_blueprint.register_blueprint(card_blueprint, url_prefix='/cards')
api_blueprint.register_blueprint(test_blueprint, url_prefix='/tests')