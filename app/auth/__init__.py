from flask import Blueprint

# Create the auth blueprint
auth_bp = Blueprint("auth", __name__)

# Import routes at the bottom to avoid circular dependencies
from app.auth import routes
