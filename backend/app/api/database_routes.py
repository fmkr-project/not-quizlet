from flask import Blueprint, jsonify
from db import my_db

database_blueprint = Blueprint('db', __name__)

@database_blueprint.route('/reset', methods=['PUT'])
def reset():
    my_db.reset()
    return jsonify({'message': 'The database has been succesfully reset.'}), 201
    