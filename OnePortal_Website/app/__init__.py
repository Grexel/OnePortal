from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

mainApp = Flask(__name__)
mainApp.config.from_object(Config)

db = SQLAlchemy(mainApp)
migrate = Migrate(mainApp, db)

login = LoginManager(mainApp)
login.login_view = 'login'

from app import routes, models