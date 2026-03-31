from flask import render_template
from app.errors import errors_bp
from app.extensions import db


@errors_bp.app_errorhandler(400)
def bad_request_error(error):
    return render_template("errors/400.html", title="Bad Request"), 400


@errors_bp.app_errorhandler(403)
def forbidden_error(error):
    return render_template("errors/403.html", title="Forbidden"), 403


@errors_bp.app_errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html", title="Page Not Found"), 404


@errors_bp.app_errorhandler(405)
def method_not_allowed_error(error):
    return render_template("errors/405.html", title="Method Not Allowed"), 405


@errors_bp.app_errorhandler(500)
def internal_error(error):
    # If a database error caused the 500, we need to rollback the session
    # so it doesn't break future requests.
    db.session.rollback()
    return render_template("errors/500.html", title="Internal Error"), 500
