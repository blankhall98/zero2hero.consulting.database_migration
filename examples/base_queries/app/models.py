from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    password = db.Column(db.String(250),nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    location = db.Column(db.String(80),nullable=False)
    description = db.Column(db.String(250),nullable=False)
    amount = db.Column(db.Integer,nullable=False)