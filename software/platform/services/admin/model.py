from __future__ import annotations

from app import db

import json

class Policy(db.Model):
	"""
	Single row DB meant to store the platform's policy settings.
	"""

	__tablename__ = "Policy"

	id  = db.Column(db.Integer, primary_key=True)

	# If True, then users are required to claim their account after first
	# logging in with their badge ID. If False, then no account claim is needed
	# in order to log in.
	requireRegistration = db.Column(db.Boolean, nullable=False)

	# If True, then users are able to self-service reset their own account via
	# an account reset email. If False, then users must go to an organizer in
	# order to reset their account.
	selfServiceAccountReset = db.Column(db.Boolean, nullable=False)

	# How many seconds an account reset token is valid for.
	selfServiceAccountResetExpiry  = db.Column(db.Integer, nullable=True)

	def __init__(
		self,
		requireRegistration=True,
		selfServiceAccountReset=False,
		selfServiceAccountResetExpiry=None
	):
		self.requireRegistration = requireRegistration
		self.selfServiceAccountReset = selfServiceAccountReset
		self.selfServiceAccountResetExpiry = selfServiceAccountResetExpiry

	def __str__(self):
		data = {
			"requireRegistration": self.requireRegistration,
			"selfServiceAccountReset": self.selfServiceAccountReset,
			"selfServiceAccountResetExpiry": self.selfServiceAccountResetExpiry,
		}
		return json.dumps(data)
