from flask_sqlalchemy import SQLAlchemy
from .views import app
import logging as lg
import enum

# Create database connection object
db = SQLAlchemy(app)

class Gender(enum.Enum):
    female = 0
    other = 1
    male = 2

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

db.create_all()

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("あの夢をなぞって", Gender['other']))
    db.session.add(Content("たぶん", Gender['female']))
    db.session.add(Content("空", Gender['other']))
    db.session.add(Content("泣く", Gender['male']))
    db.session.add(Content("ハルジオン", Gender['female']))
    db.session.commit()
    lg.warning('Database initialized!')