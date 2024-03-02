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
		data = {
			"code": self.code,
			"points": self.points,
			"id": self.id,
		}
		return json.dumps(data)

class Submission(db.Model):

	__tablename__ = "Submission"

	id = db.Column(db.Integer, primary_key=True)

	codeId = db.Column(db.Integer, unique=False, nullable=False)
	userId = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, codeId: int, userId: int):
		self.codeId = codeId
		self.userId = userId

	def __str__(self):
		data = {
			"codeId": self.codeId,
			"userId": self.userId,
			"id": self.id,
		}
		return json.dumps(data)

