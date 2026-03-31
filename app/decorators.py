from functools import wraps
from flask import abort
from flask_login import current_user


def admin_required(f):
    """
    Custom decorator to require admin privileges for a route.
    Must be placed AFTER @login_required.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If the user is not logged in, or their role is not 'admin', trigger a 403 error
        if not current_user.is_authenticated or current_user.role != "admin":
            abort(403)
        return f(*args, **kwargs)

    return decorated_function
