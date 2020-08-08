from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Create database instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# import the routes
from cbt_logger import routes
