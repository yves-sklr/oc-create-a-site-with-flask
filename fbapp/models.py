from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app

# Create database connection objet
db = SQLAlchemy(app)

class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("THIS IS SPARTAAAAA!!!", Gender['male']))
    db.session.add(Content("What's your favourite scary movie?", Gender['female']))
    db.session.commit()
    lg.warning('Database initialised!')


#db.create_all()
