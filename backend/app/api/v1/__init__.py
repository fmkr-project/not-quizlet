from flask import Blueprint
from .user_routes import users_blueprint
from .deck_routes import decks_blueprint
from .card_routes import cards_blueprint

v1_blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')
v1_blueprint.register_blueprint(users_blueprint, url_prefix='/users')
v1_blueprint.register_blueprint(decks_blueprint, url_prefix='/decks')
v1_blueprint.register_blueprint(cards_blueprint, url_prefix='/cards')