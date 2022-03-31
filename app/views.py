from flask import render_template, flash, url_for, request
from .forms import AddProduct
from .models import DbModel
from app import app, db


@app.route('/homepage')
def home_page():
    return render_template ("base.html", title="")
