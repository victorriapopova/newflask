# models.py

from app import db


class Headphone(db.Model):
    __tablename__ = 'headphones'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    image_url = db.Column(db.String(200))
