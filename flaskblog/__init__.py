from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)

app.config['SECRET_KEY'] = '858d2251646011ba1936bf8ba6600f12'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
api = Api(app)

from flaskblog import routes