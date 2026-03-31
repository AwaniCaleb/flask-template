from app.extensions import db, login_manager
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """A sample User model for the database."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)

    role = db.Column(db.String(20), nullable=False, default='user')

    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def set_password(self, password):
        """Hashes the password and saves it to the user object."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        # This tells Python how to print objects of this class, useful for debugging
        return f"<User {self.username}>"


# Flask-Login needs this to reload the user object from the session ID
@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))
