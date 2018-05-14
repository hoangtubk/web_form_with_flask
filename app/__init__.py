"""
 * Created by PyCharm.
 * User: tuhoangbk
 * Date: 10/05/2018
 * Time: 16:00
 * Have a nice day　:*)　:*)
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
