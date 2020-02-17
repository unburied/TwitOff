"""Short script to reset database"""

from .models import DB

def reset():
    DB.drop_all()
    DB.create_all()    