from flask import Blueprint, request, jsonify
from .auth import login_required
from .user_routes import get_user_id_from_token
from db import my_db
deck_blueprint = Blueprint('decks', __name__)

@deck_blueprint.route('/create', methods=['POST'])
@login_required
def create_deck():
    user_id_from_token = get_user_id_from_token()
    data = request.json
    name = data.get('name')
    description = data.get('description')
    if not name or not description or user_id_from_token is None:
        return jsonify({'error': 'Missing fields'}), 400
    if my_db.create_deck(name, description, user_id_from_token):
        return jsonify({'message': 'Deck created successfully'}), 201
    else:
        return jsonify({'error': 'Deck creation failed'}), 500

@deck_blueprint.route('/deck/modify/<int:deck_id>', methods=['PUT'])
@login_required
def modify_deck(deck_id):
    user_id_from_token = get_user_id_from_token()
    data = request.json
    name = data.get('name', None)
    description = data.get('description', None)
    deck = my_db.get_deck_by_id(deck_id)
    if deck and deck['creator_id'] == user_id_from_token:
        if my_db.modify_deck(deck_id, name, description):
            return jsonify({"message": "Deck modified successfully"}), 200
        else:
            return jsonify({"error": "Deck modification failed"}), 500
    else:
        return jsonify({"error": "Unauthorized modification attempt or deck not found"}), 403