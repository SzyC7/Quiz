from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    migrate = Migrate(app, db)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "main.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for routes routes in our app
    from .routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    # blueprint for non-routes parts of app
    from .main import base as base_blueprint

    app.register_blueprint(base_blueprint)

    return app