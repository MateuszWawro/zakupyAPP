from . import db
from sqlalchemy import String
from flask_login import UserMixin

class DbModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product = db.Column(db.String(100))
    producer = db.Column(db.String(100))
    price = db.Column(db.Numeric(3))
    ilosc = db.Column(db.Integer())



class UserModel(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(15))
    surname = db.Column(db.String(15))
    login = db.Column(db.String(15),  unique=True)
    email = db.Column(db.String(120), unique=True )
    password = db.Column(db.String(32), nullable=True)
    role = db.Column(db.Boolean())
