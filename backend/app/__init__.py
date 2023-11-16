from flask import Flask
from backend.app.api import get_api_blueprint

def create_app(config_filename, api_version) -> Flask:
    app : Flask = Flask(__name__)
    app.config.from_pyfile(config_filename)
    api_blueprint = get_api_blueprint(api_version)
    app.register_blueprint(api_blueprint)
    return app