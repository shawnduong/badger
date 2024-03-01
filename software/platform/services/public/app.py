from flask import *
#from flask_sqlalchemy import *

from helper import *

import os

# Instantiate the application and define settings.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///public.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.urandom(32)

## Load the database.
#db = SQLAlchemy(app)
#from model import *
#with app.app_context():
#	db.create_all()

from public import *
