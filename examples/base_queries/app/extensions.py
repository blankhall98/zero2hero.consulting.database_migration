from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#base configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'

#initialize the database
db = SQLAlchemy(app)