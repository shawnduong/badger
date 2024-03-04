from __future__ import annotations

from app import db

import json

class Redemption(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	entitlementId = db.Column(db.Integer, unique=False, nullable=False)
	userId        = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, entitlementId: int, userId: int):
		self.entitlementId = entitlementId
		self.userId = userId

	def __str__(self):
		return json.dumps({
			"entitlementId": self.entitlementId,
			"userId": self.userId,
			"id": self.id,
		})

