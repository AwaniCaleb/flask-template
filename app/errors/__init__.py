from flask import Blueprint

# Create the errors blueprint
errors_bp = Blueprint("errors", __name__)

# Import the handlers at the bottom to avoid circular dependencies
from app.errors import handlers
