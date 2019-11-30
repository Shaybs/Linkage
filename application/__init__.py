from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"+os.getenv("USERNAME")+":"+os.getenv("PASSWORD")+"@35.197.196.36/bookapp"
app.config['SECRET_KEY'] = 'hjd9848rujjuuIJDF84Uj*(&ye&*£KMCD938JUud(K'
db = SQLAlchemy(app)

from application import routes
