from flask import render_template, flash, url_for, request, redirect
from sqlalchemy.exc import DBAPIError
from .forms import AddProduct
from .models import DbModel
from app import app, db


@app.route('/')
def home_page():
    return render_template ("base.html", title="")


@app.route('/addproduct')
def view_add_product():
    form = AddProduct()
    product_list = DbModel.query.all()
    print(product_list)
    if form.validate_on_submit():
        try:
            q = DbModel(product=form.product.data, producer=form.producer.data, price=form.price.data)
            db.session.add(q)
        except DBAPIError as e:
            db.session.rollback()
            flash(e.detail)
        else:
            db.session.commit()
            product_list = DbModel.query.all()
            return redirect(url_for('view_add_product'))
    else:
        flash(form.errors)
        print(form.errors)
    return render_template("productadd.html", title="")


