from flask import Blueprint
from .user_routes import user_blueprint
from .deck_routes import deck_blueprint
from .card_routes import card_blueprint

api_blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')
api_blueprint.register_blueprint(user_blueprint, url_prefix='/users')
api_blueprint.register_blueprint(deck_blueprint, url_prefix='/decks')
api_blueprint.register_blueprint(card_blueprint, url_prefix='/cards')