from cbt_logger import db, login_manager
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


class Emotion(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    log_id = db.Column(db.Integer, db.ForeignKey('cbtlog.id'), nullable=False)

    def __repr__(self):
        return f"Emotion('{self.name}')"


class Distortion(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False),
    description = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f"Distortion('{self.name}')"


class CBTLog(db.Model):
    __tablename__ = "cbtlog"
    id = db.Column(db.Integer, primary_key=True)
    brief = db.Column(db.String(80), nullable=False)
    context = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    emotions = db.relationship('Emotion', backref='log', lazy=True)

    def __repr__(self):
        return f"CBTLog('{self.user_id}', '{self.brief}')"
