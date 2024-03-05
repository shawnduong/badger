from __future__ import annotations

from app import db

import json

class Scanner(db.Model):

	__tablename__ = "Scanner"

	id = db.Column(db.Integer, primary_key=True)

	scannerId = db.Column(db.Integer, unique=True , nullable=False)
	lastAlive = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, scannerId: int, lastAlive: int):
		self.scannerId = scannerId
		self.lastAlive = lastAlive

	def __str__(self):
		return json.dumps({
			"scannerId": self.scannerId,
			"lastAlive": self.lastAlive,
			"id": self.id
		})

