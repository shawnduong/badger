from __future__ import annotations

from app import db

import json

class Event(db.Model):

	__tablename__ = "Event"

	id = db.Column(db.Integer, primary_key=True)

	title        = db.Column(db.Text       , unique=False, nullable=False)
	location     = db.Column(db.Text       , unique=False, nullable=False)
	map          = db.Column(db.LargeBinary, unique=False, nullable=True )
	startTime    = db.Column(db.Integer    , unique=False, nullable=False)
	duration     = db.Column(db.Integer    , unique=False, nullable=False)
	code         = db.Column(db.String(256), unique=False, nullable=False)
	points       = db.Column(db.Integer    , unique=False, nullable=False)
	host         = db.Column(db.Text       , unique=False, nullable=False)
	description  = db.Column(db.Text       , unique=False, nullable=False)

	def __init__(
		self, title: str, location: str, map: bytes, startTime: int,
		duration: int, code: str, points: int, host: str, description: str
	):
		self.title = title
		self.location = location
		self.map = map
		self.startTime = startTime
		self.duration = duration
		self.code = code
		self.points = points
		self.host = host
		self.description = description

	def __str__(self):
		return json.dumps({
			"title": self.title,
			"location": self.location,
			"map": self.map,
			"startTime": self.startTime,
			"duration": self.duration,
			"code": self.code,
			"points": self.points,
			"host": self.host,
			"description": self.description,
		})

