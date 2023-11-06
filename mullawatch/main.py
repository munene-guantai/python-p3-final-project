from flask import Flask
from flask_sqlalchemy import sqlalchemy
from mullawatch import cli, database, models, reports

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mullawatch.db'

db = SQLAlchemy(app)

from mullawatch import models, views