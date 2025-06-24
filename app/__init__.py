from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    load_dotenv()  # load environment variables from .env

    # Make sure to get the correct env var name here!
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # <-- FIXED

    # Optional but recommended
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'app.login'  # redirect here if not logged in

    # Import and register your routes blueprint
    from app.routes import app as app_blueprint
    app.register_blueprint(app_blueprint)

    with app.app_context():
        db.create_all()  # creates tables if they don't exist

    return app
