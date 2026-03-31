import os

# Get the absolute path of the directory where config.py is located
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration."""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess-this-default-key"
    # Suppress a SQLAlchemy warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    # Setup a local SQLite database for development
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "..", "app-dev.sqlite")


class ProductionConfig(Config):
    DEBUG = False
    # In production, you would use a PostgreSQL or MySQL URL from your environment
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_by_name = dict(dev=DevelopmentConfig, prod=ProductionConfig)
