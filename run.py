import os
from app import create_app

# Load the configuration name from the environment, default to 'dev'
env = os.environ.get("FLASK_ENV", "dev")

# Create the application instance
app = create_app(env)

if __name__ == "__main__":
    app.run()
