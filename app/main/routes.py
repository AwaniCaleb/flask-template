from flask import render_template
from app.main import main_bp

@main_bp.route('/')
def index():
    """Route for the home page."""
    # We pass a dynamic variable 'title' to the Jinja template
    return render_template('index.html', title="Welcome to Flask Template")
