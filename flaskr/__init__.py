from flask import Flask

from .config import Config
from .extensions import db, migrate
from .models import load_all_models
from .views import register_blueprints


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        load_all_models()

    register_blueprints(app)

    return app
