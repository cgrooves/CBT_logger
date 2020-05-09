from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'e57e70c34719a8f6d181fc5384d8cca6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create database instance
db = SQLAlchemy(app)

from cbt_logger import routes

