from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from classes import User

class newAccount(FlaskForm):
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists! Please Try a Diffrent User')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already exists! Please Try a Diffrent Email')

    username = StringField(label='UserName:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password = PasswordField(label='PassWord:', validators=[Length(min=8), DataRequired()])
    confirm_password = PasswordField(label='Confirm PassWord:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')

class Login(FlaskForm):
    username = StringField(label='UserName:', validators=[DataRequired()])
    password = PasswordField(label='PassWord:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class Buy(FlaskForm):
    submit = SubmitField(label='Buy')

class Sell(FlaskForm):
    submit = SubmitField(label='Sell')

class Remove(FlaskForm):
    submit = SubmitField(label='Remove')

class Add(FlaskForm):
    submit = SubmitField(label='Add New Item')

class NewItem(FlaskForm):
    name = StringField(label='Name:', validators=[DataRequired()])
    price = StringField(label='Price:', validators=[DataRequired()])
    description = StringField(label='Description:', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class EditItem(FlaskForm):
    name = StringField(label='Name:', validators=[DataRequired()])
    price = StringField(label='Price:', validators=[DataRequired()])
    description = StringField(label='Description:', validators=[DataRequired()])
    submit = SubmitField(label='Edit')