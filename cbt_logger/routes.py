from flask import render_template, flash, redirect, url_for, request
from cbt_logger.forms import RegistrationForm, LoginForm, EventForm
from cbt_logger import app, bcrypt, db
from cbt_logger.models import User, CBTLog
from flask_login import login_user, logout_user, current_user, login_required


@app.route("/home")
@app.route("/", methods=['GET', 'POST'])
def home():
    # Get a list of current logs (if logged in)
    if current_user.is_authenticated:
        logs = CBTLog.query.filter_by(user_id=current_user.id).all()
    else:
        logs = []

    return render_template("home.html", title="Home", logs=logs)


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


@app.route('/log', methods=['GET', 'POST'])
@app.route('/log/<int:id>', methods=['GET', 'POST'])
@login_required
def log(id=None):
    eventForm = EventForm()

    # Validate that the current user can access this log
    if id:
        old_log = CBTLog.query.filter_by(user_id=current_user.id,
                                         id=id).first()
        if old_log is None:
            flash(f'Log {id} not found for user {current_user.username}')
            return redirect(url_for('log'))
    else:
        old_log = None

    # Handle form submission
    if eventForm.validate_on_submit():
        if old_log:
            # Update the log
            old_log.brief = eventForm.brief.data
            old_log.context = eventForm.detailed.data
            new_log = old_log
        else:
            # Get the event data and make a db entry
            new_log = CBTLog(brief=eventForm.brief.data,
                             context=eventForm.detailed.data,
                             user_id=current_user.get_id())
            db.session.add(new_log)

        # Save changes to the database
        db.session.commit()

        # Go to the next page
        return redirect(url_for('emotions', id=new_log.id))
    elif id:  # Handle update
        # Populate the form
        eventForm.detailed.data = old_log.context
        eventForm.brief.data = old_log.brief

    return render_template('event.html', title='Event', form=eventForm)


@app.route('/emotions/<int:id>', methods=['GET', 'POST'])
@login_required
def emotions(id):
    # TODO validate user access to log
    theLog = CBTLog.query.get(id)

    return render_template('emotions.html', title='Emotions',
                           log=theLog)
