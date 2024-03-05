from __future__ import annotations

from app import db, IMPLEMENTATION
from flask_login import UserMixin

import bcrypt
import json
import re
import requests
from typing import Union

class User(UserMixin, db.Model):

	PRIV_USER  = 0
	PRIV_ADMIN = 1

	__tablename__ = "User"

	id = db.Column(db.Integer, primary_key=True)

	uid        = db.Column(db.Integer    , unique=False, nullable=True )
	privilege  = db.Column(db.Integer    , unique=False, nullable=False)
	email      = db.Column(db.String(256), unique=False, nullable=True )
	password   = db.Column(db.String( 64), unique=False, nullable=True )
	points     = db.Column(db.Integer    , unique=False, nullable=True )
	claimed    = db.Column(db.Boolean    , unique=False, nullable=False)
	custom     = db.Column(db.Text       , unique=False, nullable=True )

	def __init__(
		self,
		uid: int=None,
		privilege: int=PRIV_USER,
		email: str=None,
		password: str=None,
		points: int=None,
		claimed: bool=False,
		custom: str=None
	):
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

	def update_points(self):
		"""
		Update self.points as sum(event attendance, code submission) - sum(claim).
		"""

		points = 0

		try:
			r = requests.get(IMPLEMENTATION["manage"]+f"/attendance/lookup/{self.id}")
			attendances = [json.loads(obj) for obj in json.loads(r.content)]
		except:
			return False

		for attendance in attendances:
			r = requests.get(IMPLEMENTATION["manage"]+f"/event/{attendance['eventId']}")
			if r.status_code != 200:
				continue
			points += json.loads(r.content)["points"]

		try:
			r = requests.get(IMPLEMENTATION["manage"]+f"/submission/lookup/{self.id}")
			submissions = [json.loads(obj) for obj in json.loads(r.content)]
		except:
			return False

		for submission in submissions:
			r = requests.get(IMPLEMENTATION["manage"]+f"/code/{submission['codeId']}")
			if r.status_code != 200:
				continue
			points += json.loads(r.content)["points"]

		try:
			r = requests.get(IMPLEMENTATION["manage"]+f"/claim/lookup/{self.id}")
			claims = [json.loads(obj) for obj in json.loads(r.content)]
		except:
			return False

		for claim in claims:
			r = requests.get(IMPLEMENTATION["manage"]+f"/reward/{claim['rewardId']}")
			if r.status_code != 200:
				continue
			points -= json.loads(r.content)["points"]

		self.points = points
		return points

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

