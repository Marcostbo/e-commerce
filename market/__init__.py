from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_recaptcha import ReCaptcha


class MySQLAlchemy(SQLAlchemy):
    # Can add the below code on the SQLAlchemy directly if you think to modify the package code is acceptable.
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'crazy_cupcake'

app.config['RECAPTCHA_SITE_KEY'] = 'your_site_key'
app.config['RECAPTCHA_SECRET_KEY'] = 'your_secret_key'
# for more information: https://developers.google.com/recaptcha
# tip: use recaptcha v2

db = MySQLAlchemy(app)
bcrypt = Bcrypt(app)
recaptcha = ReCaptcha(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes

