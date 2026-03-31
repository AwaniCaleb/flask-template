from flask import Flask
from .config import config_by_name
from .extensions import db, migrate


def create_app(config_name="dev"):
    """Application factory function."""
    # Initialize the Flask app
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config_by_name[config_name])

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so Flask-Migrate knows about them
    from app import models

    # Import and register Blueprints
    from app.main import main_bp

    # Import and register error handlers
    from app.errors import errors_bp
    app.register_blueprint(errors_bp)

    # Import and register the authentication Blueprint
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    app.register_blueprint(main_bp)

    return app
