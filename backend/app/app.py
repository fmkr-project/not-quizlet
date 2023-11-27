from flask import Flask, render_template, request, redirect, url_for
from os import getenv
from .api import api_blueprint
import mail
FLASK_SECRET_KEY = getenv("FLASK_SECRET_KEY")
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = FLASK_SECRET_KEY
    app.register_blueprint(api_blueprint)
    return app
my_app = create_app()
