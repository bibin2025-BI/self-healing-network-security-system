# app/__init__.py
from flask import Flask
from app.routes import app_routes
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize database
    db.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(app_routes)
    
    return app
