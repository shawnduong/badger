from __future__ import annotations

from app import db

import json

class Submission(db.Model):

	__tablename__ = "Submission"

	id = db.Column(db.Integer, primary_key=True)

	codeId = db.Column(db.Integer, unique=False, nullable=False)
	userId = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, codeId: int, userId: int):
		self.codeId = codeId
		self.userId = userId

	def __str__(self):
		return json.dumps({
			"codeId": self.codeId,
			"userId": self.userId,
			"id": self.id,
		})

