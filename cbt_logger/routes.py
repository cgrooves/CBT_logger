from flask import render_template, flash, redirect, url_for
from cbt_logger.forms import RegistrationForm, LoginForm
from cbt_logger import app

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