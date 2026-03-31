import os

class Config:
    """Base configuration."""
    # A secret key is needed for session management and form security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this-default-key'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Dictionary to easily select the configuration based on the environment
config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
