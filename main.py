from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'
db = SQLAlchemy(app)

class databasecls(db.Model):
    id = db.Column(db.Integer() , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(1024), nullable=False)

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

@app.route('/database')
@app.route('/market')
def database():
    dic = databasecls.query.all()
    return render_template('data.html', dic=dic)

