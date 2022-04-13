from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, EmailField, PasswordField, validators
from wtforms.validators import DataRequired


class AddProduct(FlaskForm):
    product = StringField('Produkt')
    producer = StringField('Producent')
    price = FloatField('Cena')
    submit = SubmitField('Dodaj')
    ilosc = FloatField('Ilość')


class RegistratonForm(FlaskForm):
    name = StringField('Imię' ,[validators.Length(min=4, max=20)])
    surname = StringField('Nazwisko', [validators.Length(min=4, max=20)])
    email = EmailField('Adres Email', [validators.Email()])
    login = StringField ('Login', [validators.Length(min=4, max=20)])
    password = PasswordField('Hasło', [validators.InputRequired()])
    submit = SubmitField('Zarejestruj się')


class LoginForm(FlaskForm):
    login = StringField('Login' ,validators=[DataRequired()])
    password = PasswordField('Hasło',validators=[DataRequired()])
    submit = SubmitField('Zaloguj')


class EditUser(FlaskForm):
    name = StringField('Imię', [validators.Length(min=4, max=20)])
    surname = StringField('Nazwisko', [validators.Length(min=4, max=20)])
    email = EmailField('Adres Email', [validators.Email()])
    login = StringField('Login', [validators.Length(min=4, max=20)])
    password = PasswordField('Hasło', [validators.InputRequired()])
    role = StringField('Rola', [validators.Length(min=1, max=1)])
    submit = SubmitField('Zarejestruj się')