from app.extensions import db
from datetime import datetime, timezone


class User(db.Model):
    """A sample User model for the database."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        # This tells Python how to print objects of this class, useful for debugging
        return f"<User {self.username}>"
