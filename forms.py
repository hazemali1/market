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
