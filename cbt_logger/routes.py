from flask import render_template, flash, redirect, url_for, request
from cbt_logger.forms import RegistrationForm, LoginForm
from cbt_logger import app, bcrypt, db
from cbt_logger.models import User
from flask_login import login_user, logout_user, current_user, login_required


@app.route("/home")
@app.route("/", methods=['GET', 'POST'])
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
        flash(f"New account creation successful! Welcome,\
            {form.username.data}!", "success")
        return redirect(url_for('home'))

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check email and password
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=False)

            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful, please check username and password.",
                  "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


@app.route("/emotions")
@login_required
def emotions():
    return render_template('emotions.html', title='Mood Logging')


@app.route("/event")
@login_required
def event():
    return render_template('event.html', title='Event')


@app.route("/thoughts")
@login_required
def thoughts():
    return render_template('thoughts.html', title='Thoughts')


@app.route("/summary")
@login_required
def summary():
    return render_template('summary.html', title='Summary')