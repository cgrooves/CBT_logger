from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'e57e70c34719a8f6d181fc5384d8cca6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# import the routes
from cbt_logger import routes
