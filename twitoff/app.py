"""Twitoff app to analyze and compare tweets"""

from flask import Flask 
from .models import DB
# create app factory

def create_app():
    app = Flask(__name__)

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # link Database to App
    DB.init_app(app)
    
    @app.route('/')
    def root():
        return 'Welcome to Twitoff'

    return app

