from __future__ import annotations

from app import db

import json

class Code(db.Model):

	__tablename__ = "Code"

	id = db.Column(db.Integer, primary_key=True)

	code   = db.Column(db.String(256), unique=True , nullable=False)
	points = db.Column(db.Integer    , unique=False, nullable=False)

	def __init__(self, code: str, points: int=0):
		self.code = code
		self.points = points

	def __str__(self):
		return json.dumps({
			"code": self.code,
			"points": self.points,
			"id": self.id,
		})

