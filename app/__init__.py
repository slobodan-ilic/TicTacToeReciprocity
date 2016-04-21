from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap
from config import config
from .model import db

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    register_app_blueprints(app)

    return app


def register_app_blueprints(app):
    from viewer.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from viewer.game import game as game_blueprint
    app.register_blueprint(game_blueprint)
    from viewer.user import user as user_blueprint
    app.register_blueprint(user_blueprint)
