from flask import Flask
from flask_cors import CORS
from config.database import configure_database
from config.api import configure_api_settings
import models

def create_app():
    app = Flask(__name__)
    
    # Configure CORS
    CORS(app, origins=['http://localhost:5000'])
    
    # Initialize components
    migrate = configure_database(app)
    api = configure_api_settings(app)
    
    # Register blueprints here
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)