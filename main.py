from flask import Flask, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'e57e70c34719a8f6d181fc5384d8cca6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create database instance
db = SQLAlchemy(app)

# Data Models


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=20), unique=True, nullable=False)
    email = db.Column(db.String(length=20), unique=True, nullable=False)
    password = db.Column(db.String(length=60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    cbt_logs = db.relationship('CBTLog', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Mood(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f"Mood('{self.name}')"


class Distortion(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False),
    description = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f"Distortion('{self.name}')"


class CBTLog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    brief = db.Column(db.String(80), nullable=False)
    context = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"CBTLog('{self.user_id}', '{self.datetime}', '{self.brief}')"

# Routing


@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(port=8992, debug=True)
