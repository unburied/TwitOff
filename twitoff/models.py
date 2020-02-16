"""Database script for app"""

from flask_sqlalchemy import SQLAlchemy 

DB = SQLAlchemy()

class User(DB.Model):
    """Users that we analyze"""

    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable = False)

class Tweet(DB.Model):
    """Tweest we pull"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))

    