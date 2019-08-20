import os
from os import urandom
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

f_bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crm.db"
    app.config["SQLALCHEMY_ECHO"] = True

app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

from functools import wraps
# oma login_required dekoraattori käyttäjän autorisointiin 
def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                if current_user.get_role() == role:
                    unauthorized = False

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


from datetime import datetime
from application import views
from application.customers import models
from application.customers import views
from application.auth import models
from application.auth import views
from application.comment import models
from application.comment import views
from application.task import models
from application.task import views
from application.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try:
    db.create_all()
except:
    pass
