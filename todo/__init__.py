from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = "info"

from todo import routes