from flask import render_template, flash, url_for, request, redirect
from flask_login import login_user, logout_user
from sqlalchemy.exc import DBAPIError
from .forms import AddProduct, RegistratonForm, LoginForm
from .models import DbModel, UserModel
from app import app, db, lm



##widok strony głównej
@app.route('/')
def home_page():
    return render_template("base.html", title="")


##widok listy produktów
@app.route('/productlist')
def view_product_list():
    product_list = DbModel.query.all()
    return render_template("productlist.html", title="", product_list=product_list)


##widok
@app.route('/database', methods=["GET"])
def view_data_base():
    return render_template("database.html", title="")


##widok formularza rejestracji
@app.route('/registrate', methods=['GET', 'POST'])
def view_registraton():
    form = RegistratonForm()
    user_list = UserModel.query.all()
    print(user_list)
    if form.validate_on_submit():
        try:
            q2 = UserModel(name=form.name.data, surname=form.surname.data, email=form.email.data, login=form.login.data, password=form.password.data)
            db.session.add(q2)
        except DBAPIError as e2:
            db.session.rollback()
            flash(e2.detail)
        else:
            db.session.commit()
            UserModel.query.all()
            return redirect(url_for('home_page'))
    else:
        flash(form.errors)
        print(form.errors)

    return render_template("registratonform.html", title="", form=form, user_list=user_list if user_list else list)


##widok formularza dodawania produktów
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


##widok formularz logowania
@app.route('/login', methods=['GET', 'POST'])
def view_login():
    form = LoginForm()
    if form.validate_on_submit():
        login = UserModel.query.filter_by(login=form.login.data).first()
        if login and login.password == form.password.data:
            login_user(login)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home_page'))
        flash('złe hasło lub login')
        return redirect(url_for('home_page'))
    return render_template('loginform.html', form=form)


@lm.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)


##wylogowywanie użytkownika
@app.route('/logout')
def view_logout():
    logout_user()
    return redirect(url_for('home_page'))


##kasowanie rekordów
@app.route("/delete/<int:id>", methods=["POST","GET"])
def view_delete(id):
    product_list = DbModel.query.filter_by(id=id).first()
    db.session.delete(product_list)
    db.session.commit()
    return redirect(url_for('view_product_list'))
