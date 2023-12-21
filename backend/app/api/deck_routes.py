from flask import Blueprint, request, jsonify, g
from .auth import login_required
from .user_routes import get_user_id_from_token
from db import my_db
deck_blueprint = Blueprint('decks', __name__)

@deck_blueprint.route('/create', methods=['POST'])
@login_required
def create_deck():
    user_id_from_token = getattr(g, 'user_id_from_token', None)
    data = request.json
    name = data.get('name')
    description = data.get('description')
    if not name or not description or not user_id_from_token:
        return jsonify({'error': 'Missing fields'}), 400
    if my_db.create_deck(name, description, user_id_from_token):
        return jsonify({'message': 'Deck created successfully'}), 201
    else:
        return jsonify({'error': 'Deck creation failed'}), 500

@deck_blueprint.route('/deck/modify/<int:deck_id>', methods=['PUT'])
@login_required
def modify_deck(deck_id):
    user_id_from_token = getattr(g, 'user_id_from_token', None)
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
    
@deck_blueprint.route('/public_decks', methods=['GET'])
def get_public_decks():
    decks = my_db.get_public_decks()
    if decks is not None:
        return jsonify({'decks': decks}), 200
    else:
        return jsonify({'error': 'No public decks found'}), 404
    
@deck_blueprint.route('/<int:deck_id>/flashcards', methods=['GET'])
def get_flashcards(deck_id):
    try:
        flashcards = my_db.get_flashcards_by_deck_id(deck_id)
        if flashcards:
            # Assuming your 'execute' method returns a list of dictionaries
            return jsonify({'flashcards': flashcards}), 200
        else:
            return jsonify({'message': 'No flashcards found for this deck'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@deck_blueprint.route('/get_user_decks', methods=['GET'])
@login_required
def get_user_decks():
    user_id_from_token = getattr(g, 'user_id_from_token', None)
    decks = my_db.get_all_decks_user(user_id_from_token)
    return jsonify({'decks': decks}), 200
