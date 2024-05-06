from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class newAccount(FlaskForm):
    username = StringField(label='UserName:')
    email = StringField(label='Email:')
    password = PasswordField(label='PassWord:')
    confirm_password = PasswordField(label='Confirm PassWord:')
    submit = SubmitField(label='Create Account')
