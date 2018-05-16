from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.celery_config import make_celery
from flask_mail import Mail
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '858d2251646011ba1936bf8ba6600f12'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379',
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
api = Api(app)
celery = make_celery(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog import routes