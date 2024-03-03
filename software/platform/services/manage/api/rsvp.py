from app import *

@app.route(API+"/rsvp", methods=["GET"])
@failsafe_500
def rsvp_get():

	rsvps = [str(r) for r in Rsvp.query.all()]
	return rsvps, 200

@app.route(API+"/rsvp", methods=["POST"])
@failsafe_500
def rsvp_post():

	try:
		# These are required fields for this method.
		for k in ("userId", "eventId"):
			assert k in request.json.keys()

		userId = int(request.json["userId"])
		eventId = int(request.json["eventId"])
	except:
		return {}, 400

	# It is the responsibility of the caller to make sure that the user exists
	# and return a 404 if not.
	try:
		assert Event.query.get(eventId)
	except:
		return {}, 404

	# This RSVP must be unique.
	try:
		r = Rsvp.query.filter_by(userId=userId, eventId=eventId).all()
		assert len(r) == 0
	except:
		return {}, 409

	db.session.add(Rsvp(userId, eventId))
	db.session.commit()
	return {}, 201
