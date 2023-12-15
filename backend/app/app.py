from flask import Flask
from os import getenv
from .api import api_blueprint
from flask_caching import Cache
FLASK_SECRET_KEY = getenv("FLASK_SECRET_KEY")
def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = FLASK_SECRET_KEY
    app.config['DEBUG'] = True
    app.config['CACHE_TYPE'] = 'SimpleCache' 
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300  

    app.register_blueprint(api_blueprint)
    app.cache = Cache(app)
    return app

def print_routes(app : Flask):
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        print(f"{rule.endpoint}: {rule.rule} [{methods}]")

