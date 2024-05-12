from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'
app.config['SECRET_KEY'] = '95d4cf52de5b8acf5cf83112'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

import main