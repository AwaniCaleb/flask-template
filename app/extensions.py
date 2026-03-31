from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize the extensions here, but do not bind them to the app yet.
# This prevents circular import errors in your blueprints.
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

# Tell Flask-Login which route handles log ins. 
# This automatically redirects unauthorized users here if they try to access a protected page.
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'