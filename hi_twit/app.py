from flask import Flask

def create_app():
    """create and define an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "Who twits the twitters?"
    
    return app