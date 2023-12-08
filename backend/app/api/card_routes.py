from flask import Blueprint, request, jsonify
from .auth import login_required
from .user_routes import get_user_id_from_token
from db import my_db
card_blueprint = Blueprint('cards', __name__)

@card_blueprint.route('/create', methods=['POST'])
@login_required
def create_card():
    user_id = get_user_id_from_token()
    data = request.json
    front_side = data.get('front_side')
    back_side = data.get('back_side')
    if user_id is None or not front_side or not back_side:
        return jsonify({f'error': 'Missing fields'}), 400
    if my_db.create_card(front_side, back_side, user_id):
        return jsonify({'message': 'Successfully created card'}), 201
    else:
        return jsonify({'error': 'Card creation failed'}), 500
    
@card_blueprint.route('/modify/<int:card_id>', methods=['PUT'])
@login_required
def modify_card(card_id):
    user_id = get_user_id_from_token()
    data = request.json
    new_front_side = data.get('new_front_side')
    new_back_side = data.get('new_back_side')
    card = my_db.get_card_by_id(card_id)
    if card and card['creator_id'] == user_id:
        if my_db.modify_card(card_id, new_front_side, new_back_side):
            return jsonify({"message": "Card modified successfully"}), 200
        else:
            return jsonify({"error": "Card modification failed"}), 500
    else:
        return jsonify({"error": "Unauthorized modification attempt or card not found"}), 403