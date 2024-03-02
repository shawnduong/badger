from __future__ import annotations

from app import db
from flask_login import UserMixin

import bcrypt
import json
import re
from typing import Union

class User(UserMixin, db.Model):

	PRIV_USER  = 0
	PRIV_ADMIN = 1

	__tablename__ = "User"

	id  = db.Column(db.Integer, primary_key=True)

	uid        = db.Column(db.Integer    , unique=False, nullable=True )
	privilege  = db.Column(db.Integer    , unique=False, nullable=False)
	email      = db.Column(db.String(256), unique=False, nullable=True )
	password   = db.Column(db.String( 64), unique=False, nullable=True )
	points     = db.Column(db.Integer    , unique=False, nullable=True )
	claimed    = db.Column(db.Boolean    , unique=False, nullable=False)
	custom     = db.Column(db.Text       , unique=False, nullable=True )

	def __init__(self, uid=None, privilege=PRIV_USER, email=None, password=None,
		points=None, claimed=False, custom=None):
		"""
		Create a user account. Not all information needs to be defined, just the
		privilege level and claimed status. Normal users can fill out the rest
		of the info when they claim their account.
		"""

		self.uid       = uid
		self.privilege = privilege
		self.email     = email
		self.password  = password
		self.points    = points
		self.claimed   = claimed
		self.custom    = custom

	def claim(self, email: str, password: str, custom: str) -> bool:
		"""
		Claim (as in register) an account by setting up its details. Return True
		if successful.
		"""

		pattern = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
		if not re.match(pattern, email):
			return False

		self.email = email
		self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt(4))

		# custom is currently unused, but this is where you would set up checks
		# for it if it were to be used.
		self.custom = None

		self.claimed = True

		return True

	def get_user(id: int) -> Union[User, None]:
		"""
		Get a user using their ID. 
		"""

		return User.query.filter_by(id=id).first()

	def login(uid: int, password: str) -> Union[User, None]:
		"""
		Log into an account using the badge ID and password.
		"""

		try:
			assert (user:=User.query.filter_by(uid=uid).first()) != None
			# TODO, proper check for policy on passwords.
#			if policy requires a password:
			if True:
				assert bcrypt.checkpw(password.encode(), user.password)
			return user
		except:
			return None

	def __str__(self):
		data = {
			"uid": self.uid,
			"email": self.email,
			"points": self.points,
			"claimed": self.claimed,
			"custom": self.custom,
			"privilege": self.privilege,
			"id": self.id,
		}
		return json.dumps(data)

