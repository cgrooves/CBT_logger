from cbt_logger import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=20), unique=True, nullable=False)
    email = db.Column(db.String(length=20), unique=True, nullable=False)
    password = db.Column(db.String(length=60), nullable=False)
    cbt_logs = db.relationship('CBTLog', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def get_id(self):
        return self.id


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
        return f"CBTLog('{self.datetime}', '{self.user_id}', '{self.brief}')"
