from __future__ import annotations

from app import db

import json

class Configuration(db.Model):

	__tablename__ = "Configuration"

	id = db.Column(db.Integer, primary_key=True)

	scannerId = db.Column(db.Integer, unique=True , nullable=False)
	schedule  = db.Column(db.Text   , unique=False, nullable=False)

	def __init__(self, scannerId: int, schedule: list):
		self.scannerId = scannerId
		self.schedule  = json.dumps(schedule)

	def __str__(self):
		return json.dumps({
			"scannerId": self.scannerId,
			"schedule": json.loads(self.schedule),
			"id": self.id,
		})

