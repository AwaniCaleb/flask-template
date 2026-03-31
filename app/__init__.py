from flask import Flask
from .config import config_by_name

def create_app(config_name='dev'):
    """Application factory function."""
    # Initialize the Flask app
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config_by_name[config_name])

    # Import and register Blueprints
    from app.main import main_bp
    app.register_blueprint(main_bp)

    return app
