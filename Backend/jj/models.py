#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://larry:pass@localhost/flask'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary)