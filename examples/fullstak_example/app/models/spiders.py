from app import db
from flask_login import UserMixin

class Spider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scientific_name = db.Column(db.String(120), nullable=False)
    characteristic_1 = db.Column(db.String(120), nullable=False)
    characteristic_2 = db.Column(db.String(120), nullable=False)
    characteristic_3 = db.Column(db.String(120), nullable=False)