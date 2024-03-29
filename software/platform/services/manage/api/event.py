from app import *

@app.route(API+"/event", methods=["GET"])
@failsafe_500
def event_get():
	events = [str(e) for e in Event.query.all()]
	return events, 200

@app.route(API+"/event/<eventId>", methods=["GET"])
@failsafe_500
# nodoc
def event_get_specific(eventId: int):

	try:
		assert (e:=Event.query.get(eventId))
		return str(e), 200
	except:
		return {}, 404

@app.route(API+"/event/lookup/<code>", methods=["GET"])
@failsafe_500
# nodoc
def event_get_lookup(code: str):

	event = Event.query.filter_by(code=code).first()

	try:
		assert event
		return str(event), 200
	except:
		pass

	return {}, 404

@app.route(API+"/event", methods=["POST"])
@failsafe_500
def event_post():

	try:
		# These are required fields for this method.
		for k in (
			"title", "location", "map", "startTime", "duration", "code",
			"points", "host", "description"
		):
			assert k in request.json.keys()

		startTime  = int(request.json["startTime"])
		duration   = int(request.json["duration"])
		points     = int(request.json["points"])
	except:
		return {}, 400

	db.session.add(Event(
		request.json["title"], request.json["location"], request.json["map"],
		startTime, duration, request.json["code"], points, request.json["host"],
		request.json["description"]
	))
	db.session.commit()
	return {}, 201

@app.route(API+"/event/<eventId>", methods=["PATCH"])
@failsafe_500
def event_patch(eventId: int):

	try:
		# These are required fields for this method.
		for k in (
			"title", "location", "map", "startTime", "duration", "code",
			"points", "host", "description"
		):
			assert k in request.json.keys()

		startTime  = int(request.json["startTime"])
		duration   = int(request.json["duration"])
		points     = int(request.json["points"])
	except:
		return {}, 400

	try:
		e = Event.query.get(eventId)
		assert e
	except:
		return {}, 404

	e.title       = request.json["title"]
	e.location    = request.json["location"]
	e.map         = request.json["map"]
	e.startTime   = startTime
	e.duration    = duration
	e.code        = request.json["code"]
	e.points      = points
	e.host        = request.json["host"]
	e.description = request.json["description"]
	db.session.commit()

	return {}, 200

@app.route(API+"/event/<eventId>", methods=["DELETE"])
@failsafe_500
def event_delete(eventId: int):

	try:
		e = Event.query.get(eventId)
		assert e
	except:
		return {}, 404

	db.session.delete(e)
	db.session.commit()

	return {}, 200

