from __future__ import annotations

from app import db

import json

class Announcement(db.Model):

	__tablename__ = "Announcement"

	id = db.Column(db.Integer, primary_key=True)

	timestamp  = db.Column(db.Integer, unique=False, nullable=False)
	body       = db.Column(db.Text   , unique=False, nullable=False)
	author     = db.Column(db.Text   , unique=False, nullable=False)

	def __init__(self, timestamp: int, body: str, author: str):
		self.timestamp = timestamp
		self.body = body
		self.author = author

	def __str__(self):
		return json.dumps({
			"timestamp": self.timestamp,
			"body": self.body,
			"author": self.author,
			"id": self.id,
		})

