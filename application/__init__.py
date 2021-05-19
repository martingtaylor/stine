from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField
from os import getenv

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://martin:My_Password2@34.105.132.205:3306/TESTDB' # Set the connection string to connect to the database

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("STINE_CONNECT")
app.config['SECRET_KEY'] = getenv("STINE_SECRET_KEY")



db = SQLAlchemy(app)

from application import routes

