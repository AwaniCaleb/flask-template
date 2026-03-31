from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the extensions here, but do not bind them to the app yet.
# This prevents circular import errors in your blueprints.
db = SQLAlchemy()
migrate = Migrate()
