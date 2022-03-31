from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class AddProduct(FlaskForm):
    product = StringField('Produkt')
    producer = StringField('Producent')
    price = IntegerField('Cena')
    submit = SubmitField("Dodaj")



## class AddQuantity(FlaskForm):

