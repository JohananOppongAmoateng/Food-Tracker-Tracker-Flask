from unittest.util import _MAX_LENGTH
from . import db

class Food(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    food_item = db.Column(db.String(200))
    carbohydrates = db.Column(db.Integer)
    proteins = db.Column(db.Integer)
    fats = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.Foreignkey('user.id'))


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    foods = db.relationship('Food')
    