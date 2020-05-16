from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms import TextAreaField, DateTimeField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from cbt_logger.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(2, 20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username is already taken. Please choose\
                another username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email is already registered. Please use\
                another email.")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Login')


class EventForm(FlaskForm):
    datetime = DateTimeField(label='Date/Time of Incident',
                             validators=[DataRequired()])
    brief = TextField(label='Brief Description', validators=[DataRequired()])
    detailed = TextAreaField(label='Detailed description of context',
                             validators=[DataRequired()])
    submit = SubmitField(label='Next')
