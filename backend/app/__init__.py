from .app import create_app

#def create_app(config_filename = "config/development.py") -> Flask:
    #app : Flask = Flask(__name__)
    #app.config.from_pyfile(config_filename)
    #app.register_blueprint(api_blueprint)
    #return app
my_app = create_app()