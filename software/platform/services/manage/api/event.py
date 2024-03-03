from app import *

@app.route(API+"/event", methods=["GET"])
@failsafe_500
def event_get():

	events = [str(a) for a in Event.query.all()]
	return events, 200

@app.route(API+"/event", methods=["POST"])
@failsafe_500
def event_post():

	try:
		# These are required fields for this method.
		for k in (
			"title", "location", "map", "startTime", "duration", "points",
			"host", "description"
		):
			assert k in request.json.keys()

		startTime = int(request.json["startTime"])
		duration  = int(request.json["duration"])
		points    = int(request.json["points"])
	except:
		return {}, 400

	db.session.add(Event(
		request.json["title"], request.json["location"], request.json["map"],
		startTime, duration, points, request.json["host"], request.json["description"]
	))
	db.session.commit()
	return {}, 201

#@app.route(API+"/event/<eventId>", methods=["PATCH"])
#@failsafe_500
#def event_patch(eventId: int):
#
#	try:
#		# These are required fields for this method.
#		for k in ("timestamp", "body", "author"):
#			assert k in request.json.keys()
#		timestamp = int(request.json["timestamp"])
#	except:
#		return {}, 400
#
#	try:
#		a = Event.query.get(eventId)
#		assert(a)
#	except:
#		return {}, 404
#
#	a.timestamp = timestamp
#	a.body = request.json["body"]
#	a.author = request.json["author"]
#	db.session.commit()
#
#	return {}, 200
#
#@app.route(API+"/event/<eventId>", methods=["DELETE"])
#@failsafe_500
#def event_delete(eventId: int):
#
#	try:
#		a = Event.query.get(eventId)
#		assert(a)
#	except:
#		return {}, 404
#
#	db.session.delete(a)
#	db.session.commit()
#
#	return {}, 200
#
