from flask import render_template, flash, redirect, url_for
from cbt_logger.forms import RegistrationForm, LoginForm
from cbt_logger import app, bcrypt, db
from cbt_logger.models import User

# Routing


@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    # Successful info creation
    if form.validate_on_submit():
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).\
            decode('utf-8')
        # Create a new User instance and add to database
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"New account creation successful! Welcome, {form.username.data}\
            !", "success")
        return redirect(url_for('home'))

    return render_template("register.html", title="Register", form=form)


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("login.html", title="Login", form=form)