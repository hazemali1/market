from classes import databasecls, User
from app import app, db
from functools import wraps
from flask import abort, render_template, redirect, url_for, flash, request
from forms import newAccount, Login, Buy, Sell, Remove, Add, NewItem, EditItem
from flask_login import login_user, logout_user, login_required, current_user



@app.route('/index')
def hello_world():
    return '<h1>Hello World!!!</h1>'

@app.route('/zoome')
def zoome():
    return "<h2>i love you zoome :)</h2>"

@app.route('/say/<name>')
def sayMyName(name):
    return f"<h3>{name}</h3>"

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/sayfromtemplate/<name>')
def sayfromtemplate(name):
    return render_template('name.html', name=name)

@app.route('/data')
def data():
    dic = [
        {"id": 1, "name": "phone", "price": 500, "description": "This is a greatest phone you can ever know 'it's lie :)'"},
        {"id": 2, "name": "labtop", "price": 1000, "description": "This is a greatest laptob you can ever know 'it's lie :)'"},
        {"id": 3, "name": "PC", "price": 2500, "description": "This is a greatest PC you can ever know 'it's lie :)'"},
        {"id": 4, "name": "headphone", "price": 150, "description": "This is a greatest headphone you can ever know 'it's lie :)'"}
    ]
    return render_template('data.html', dic=dic)

@app.route('/database', methods=['GET', 'POST'])
@app.route('/market', methods=['GET', 'POST'])
@login_required
def database():
    Buy_form = Buy()
    Sell_form = Sell()
    # if Buy_form.validate_on_submit():
    #     print(request.form.get('item_id'))
    # To Avoid Message when refresh Page "The page that you're looking for used information that you entered. Returning to that page might cause any action you took to be repeated. Do you want to continue?"
    if request.method == "POST":
        item_id = request.form.get('item_id')
        item = databasecls.query.filter_by(id=item_id).first()
        item_sell_id = request.form.get('item_sell_id')
        item_sell = databasecls.query.filter_by(id=item_sell_id).first()
        if item:
            if item.price <= current_user.budget:
                current_user.budget -= item.price
                item.owner = current_user.id
                db.session.commit()
                return redirect(url_for('database'))
            else:
                flash('You Dont Have Enough Budget')
                return redirect(url_for('database'))
        if item_sell:
            if item_sell in current_user.items:
                current_user.budget += item_sell.price
                item_sell.owner = None
                db.session.commit()
                return redirect(url_for('database'))

    if request.method == "GET":
        dic = databasecls.query.filter_by(owner=None)
        owned_items = databasecls.query.filter_by(owner=current_user.id)
        return render_template('data.html', dic=dic, owned_items=owned_items, Buy_form=Buy_form, Sell_form=Sell_form)

@app.route('/NewAccount', methods=['GET', 'POST'])
def NewAccount():
    form = newAccount()
    if form.validate_on_submit():
        obj = User(username=form.username.data,
                   email=form.email.data,
                   password_hash=form.password.data)
        db.session.add(obj)
        db.session.commit()
        login_user(obj)
        return redirect(url_for('database'))
    if form.errors != {}:
        for e in form.errors.values():
            flash(f'There Is Error: {e}')
    return render_template('newAccount.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('database'))
        else:
            flash('Invalid UserName or Password')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You Have Been Logged Out')
    return redirect(url_for('index'))

def only_admain(username):
    def decorator(view_function):
        @wraps(view_function)
        def decorator_function(*args, **kwargs):
            if current_user.is_authenticated and current_user.username == username:
                return view_function(*args, **kwargs)
            else:
                abort(403)
        return decorator_function
    return decorator

@app.route('/admain', methods=['GET', 'POST'])
@login_required
@only_admain('admain')
def admain():
    Buy_form = Remove()
    Sell_form = Sell()
    Add_form = Add()
    Edit_form = EditItem()
    if request.method == "POST":
        item_id = request.form.get('item_id')
        item = databasecls.query.filter_by(id=item_id).first()
        item_id_remove = request.form.get('item_id_remove')
        item_remove = databasecls.query.filter_by(id=item_id_remove).first()
        Adding = request.form.get('Adding')
        Editting = request.form.get('item_edit_id')
        if item:
            if item.price <= current_user.budget:
                current_user.budget -= item.price
                item.owner = current_user.id
                db.session.commit()
                return redirect(url_for('admain'))
            else:
                flash('You Dont Have Enough Budget')
                return redirect(url_for('admain'))
        if item_remove:
            db.session.delete(item_remove)
            db.session.commit()
            return redirect(url_for('admain'))
        if Adding:
            return redirect(url_for('newitem'))
        if Editting:
            item_to_edit = databasecls.query.filter_by(id=Editting).first()
            item_to_edit.name = Edit_form.name.data
            item_to_edit.price = Edit_form.price.data
            item_to_edit.description = Edit_form.description.data
            db.session.commit()
            return redirect(url_for('admain'))

    if request.method == "GET":
        dic = databasecls.query.filter_by(owner=None)
        owned_items = databasecls.query.filter(databasecls.owner.isnot(None)).all()
        return render_template('admain.html', dic=dic, owned_items=owned_items, Buy_form=Buy_form, Sell_form=Sell_form, Add_form=Add_form, Edit_form=Edit_form)

@app.route('/newitem', methods=['GET', 'POST'])
@login_required
@only_admain('admain')
def newitem():
    form = NewItem()
    if form.validate_on_submit():
        obj = databasecls(name=form.name.data, price=form.price.data, description=form.description.data)
        db.session.add(obj)
        db.session.commit()

        return redirect(url_for('admain'))
    return render_template('newitem.html', form=form)
