from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField


class AddProduct(FlaskForm):
    product = StringField('Produkt')
    producer = StringField('Producent')
    price = FloatField('Cena')
    submit = SubmitField('Dodaj')
    ilosc = FloatField('Ilość')



## class AddQuantity(FlaskForm):

