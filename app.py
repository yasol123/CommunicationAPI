from flask import Flask
from controllers.email_controller import email_controller
from controllers.sfmc_controller import sfmc_controller
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Optionally, you can access environment variables directly
flask_env = os.getenv('FLASK_ENV')
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(email_controller, url_prefix='/api')
app.register_blueprint(sfmc_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
