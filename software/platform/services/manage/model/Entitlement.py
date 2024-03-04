from __future__ import annotations

from app import db

import json

class Entitlement(db.Model):

	__tablename__ = "Entitlement"

	id = db.Column(db.Integer, primary_key=True)

	title     = db.Column(db.String(256), unique=True , nullable=False)
	quantity  = db.Column(db.Integer    , unique=False, nullable=False)

	def __init__(self, title: str, quantity: int):
		self.title = title
		self.quantity = quantity

	def __str__(self):
		return json.dumps({
			"title": self.title,
			"quantity": self.quantity,
			"id": self.id,
		})

