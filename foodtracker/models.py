from . import db

class Food(db.Model):
    id = db.Column(db.Integer,primary_key=True)

# class User(db.Model):
#     id