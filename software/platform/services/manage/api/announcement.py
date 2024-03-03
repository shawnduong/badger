from app import *

@app.route(API+"/announcement", methods=["POST"])
@failsafe_500
def announcement_post():

	try:
		# These are required fields for this method.
		for k in ("timestamp", "body", "author"):
			assert k in request.json.keys()
		timestamp = int(request.json["timestamp"])
	except:
		return {}, 400

	db.session.add(Announcement(timestamp, request.json["body"], request.json["author"]))
	db.session.commit()
	return {}, 201

