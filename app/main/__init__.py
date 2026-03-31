from flask import Blueprint

# Create the blueprint object
main_bp = Blueprint('main', __name__)

# Import routes at the bottom to avoid circular dependencies
from app.main import routes
