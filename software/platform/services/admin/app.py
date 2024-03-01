import os

from flask import *
from flask_sqlalchemy import *

# Instantiate the application and define settings.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///admin.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.urandom(32)

# Load the database.
db = SQLAlchemy(app)
from model import *
with app.app_context():
	db.create_all()
	# If a policy does not already exist, create a default one.
	if len(Policy.query.all()) == 0:
		db.session.add(Policy())
		db.session.commit()

from helper import *
from admin import *
