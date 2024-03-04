from __future__ import annotations

from app import db

import json

class Claim(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	rewardId  = db.Column(db.Integer, unique=False, nullable=False)
	userId    = db.Column(db.Integer, unique=False, nullable=False)
	retrieved = db.Column(db.Boolean, unique=False, nullable=False)

	def __init__(self, rewardId: int, userId: int, retrieved: bool):
		self.rewardId = rewardId
		self.userId = userId
		self.retrieved = retrieved

	def __str__(self):
		return json.dumps({
			"rewardId": self.rewardId,
			"userId": self.userId,
			"retrieved": self.retrieved,
			"id": self.id
		})

