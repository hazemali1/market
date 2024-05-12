from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class newAccount(FlaskForm):
    username = StringField(label='UserName:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password = PasswordField(label='PassWord:', validators=[Length(min=8), DataRequired()])
    confirm_password = PasswordField(label='Confirm PassWord:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')
