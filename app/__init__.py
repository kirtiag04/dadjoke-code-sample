#!flask/bin/python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialize Flask
app = Flask(__name__)
app.config.from_object('config')

# Init SQLAlchemy and Flask-Script
db = SQLAlchemy(app)

from app import routes, models