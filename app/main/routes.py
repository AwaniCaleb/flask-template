from flask import render_template
from flask_login import login_required, current_user
from app.main import main_bp
from app.decorators import admin_required


@main_bp.route("/")
def index():
    """Route for the home page."""
    return render_template("index.html", title="Welcome to Flask Template")


# A route protected by login_required
@main_bp.route("/dashboard")
@login_required
def dashboard():
    """A protected dashboard page for logged-in users."""
    return render_template("dashboard.html", title="Dashboard")


# A route protected by BOTH login_required and admin_required
@main_bp.route("/admin")
@login_required
@admin_required
def admin_panel():
    """A highly protected admin panel page."""
    return render_template("admin.html", title="Admin Panel")
