"""Database script for app"""

from flask_sqlalchemy import SQLAlchemy 

DB = SQLAlchemy()

class User(DB.Model):
    """Users that we analyze"""

    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)
    
    def __repr__(self):
        return f'<User {self.name}>'

class Tweet(DB.Model):
    """Tweest we pull"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets'), lazy=True)

    embedding = DB.Column(DB.PickleType, nullable=False)

    def __repr__(self):
        return f'<Tweet {self.text}>'

