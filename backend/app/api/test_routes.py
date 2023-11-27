from flask import Blueprint, request, jsonify
test_blueprint = Blueprint('tests', __name__)
@test_blueprint.route('/hello', methods=['GET'])
def say_hello():
    return jsonify({"hello" : "the api works!"})