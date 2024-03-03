from __future__ import annotations

from app import db

import json

class Attendance(db.Model):

	__tablename__ = "Attendance"

	id = db.Column(db.Integer, primary_key=True)

	userId  = db.Column(db.Integer, unique=False, nullable=False)
	eventId = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, userId: int, eventId: int):
		self.userId = userId
		self.eventId = eventId

	def __str__(self):
		return json.dumps({
			"userId": self.userId,
			"eventId": self.eventId,
			"id": self.id,
		})

