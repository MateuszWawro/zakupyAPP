from flask import render_template, flash, url_for, request, redirect
from sqlalchemy.exc import DBAPIError
from .forms import AddProduct
from .models import DbModel
from app import app, db


@app.route('/')
def home_page():
    return render_template ("base.html", title="")


@app.route('/productlist')
def view_product_list():
    return render_template("productlist.html", title="")


@app.route('/database', methods=["GET"])
def view_data_base():
    return render_template("database.html", title="")


@app.route('/addproduct', methods=['GET', 'POST'])
def view_add_product():
    form = AddProduct()
    product_list = DbModel.query.all()
    print(product_list)
    if form.validate_on_submit():
        try:
            q = DbModel(product=form.product.data, producer=form.producer.data, price=form.price.data, ilosc=form.ilosc.data)
            db.session.add(q)
        except DBAPIError as e:
            db.session.rollback()
            flash(e.detail)
        else:
            db.session.commit()
            DbModel.query.all()
            return redirect(url_for('view_add_product'))
    else:
        flash(form.errors)
        print(form.errors)
    return render_template("addingform.html", title="", form=form, product_list=product_list if product_list else list())


@app.route("/update/<int:id>", methods=["POST", "GET"])
def view_update(id):
    prod_list = DbModel.query.filter_by(id=id).first()
    print(prod_list)
    prod_list.complete = not prod_list.complete
    db.session.commit()
    return redirect(url_for("view_product_list"))


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def view_delete(id):
    prod_list = DbModel.query.filter_by(id=id).first()
    db.session.delete(prod_list)
    db.session.commit()
    return redirect(url_for("view_product_list"))
