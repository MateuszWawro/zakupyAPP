from . import db


class DbModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product = db.Column(db.String(100))
    producer = db.Column(db.String(100))
    price = db.Column(db.Numeric(3))
    ilosc = db.Column(db.Integer())

