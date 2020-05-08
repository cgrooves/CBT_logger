from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

##
# Basic Registration form
#
class RegistrationForm(FlaskForm):
    username = StringField('Username', \
        validators=[DataRequired(), Length(2,20)])
    email = StringField('Email', \
        validators=[DataRequired(), Email()])
    password = PasswordField('Password', \
        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', \
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

##
# Basic login form
#
class LoginForm(FlaskForm):
    email = StringField('Email', \
        validators=[DataRequired(), Email()])
    password = PasswordField('Password', \
        validators=[DataRequired()])
    submit = SubmitField('Login')