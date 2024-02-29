import os

from flask import *
#from flask_sqlalchemy import *

# Instantiate the application and define settings.
app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.urandom(32)

# Define the implementation locations.
IMPLEMENTATION = {
	"public"  : "http://localhost:64094/api/v1/public",
	"user"    : "http://localhost:64095/api/v1/user",
	"manage"  : "http://localhost:64096/api/v1/manage",
	"admin"   : "http://localhost:64097/api/v1/admin",
	"scanner" : "http://localhost:64098/api/v1/scanner",
}

## Load the database.
#db = SQLAlchemy(app)
#from model import *
#with app.app_context():
#	db.create_all()

#from security import *
from route import *
from api import *
