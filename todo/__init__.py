from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from todo import routes, models