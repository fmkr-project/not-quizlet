from flask import Flask
from os import getenv
from .api import api_blueprint, my_mail
FLASK_SECRET_KEY = getenv("FLASK_SECRET_KEY")
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = FLASK_SECRET_KEY
    app.config['DEBUG'] = True
    app.register_blueprint(api_blueprint)
    my_mail.init_app(app)
    return app
