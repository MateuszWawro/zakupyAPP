from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from contextlib import suppress

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\mwawro\\PycharmProjects\\zakupyAPP\\zakupyAPP_database.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Mateusz-DELL\\PycharmProjects\\zakupyAPP\\zakupyAPP_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'the random string'


db = SQLAlchemy(app)

from . import views, models