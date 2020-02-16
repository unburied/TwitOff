"""Twitoff app to analyze and compare tweets"""

from flask import Flask 

# create app factory

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff'

    return app
