from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\mwawro\\PycharmProjects\\zakupyAPP\\zakupyAPP_database.db'


db = SQLAlchemy