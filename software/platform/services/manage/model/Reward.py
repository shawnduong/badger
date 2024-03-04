from __future__ import annotations

from app import db

import json

class Reward(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	item       = db.Column(db.String(256), unique=True , nullable=False)
	points     = db.Column(db.Integer    , unique=False, nullable=False)
	stockTotal = db.Column(db.Integer    , unique=False, nullable=False)

	def __init__(self, item: str, points: int, stockTotal: int):
		self.item = item
		self.points = points
		self.stockTotal = stockTotal

	def __str__(self):
		return json.dumps({
			"item": self.item,
			"points": self.points,
			"stockTotal": self.stockTotal,
			"stockRemaining": 10, # TODO CALCULATE
			"id": self.id
		})

