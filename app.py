from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'
app.config['SECRET_KEY'] = '95d4cf52de5b8acf5cf83112'
db = SQLAlchemy(app)

import main