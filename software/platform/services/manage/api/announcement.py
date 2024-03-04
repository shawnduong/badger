from app import *

@app.route(API+"/announcement", methods=["GET"])
@failsafe_500
def announcement_get():
	announcements = [str(a) for a in Announcement.query.all()]
	return announcements, 200

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

@app.route(API+"/announcement/<announcementId>", methods=["PATCH"])
@failsafe_500
def announcement_patch(announcementId: int):

	try:
		# These are required fields for this method.
		for k in ("timestamp", "body", "author"):
			assert k in request.json.keys()
		timestamp = int(request.json["timestamp"])
	except:
		return {}, 400

	try:
		a = Announcement.query.get(announcementId)
		assert a
	except:
		return {}, 404

	a.timestamp = timestamp
	a.body = request.json["body"]
	a.author = request.json["author"]
	db.session.commit()

	return {}, 200

@app.route(API+"/announcement/<announcementId>", methods=["DELETE"])
@failsafe_500
def announcement_delete(announcementId: int):

	try:
		a = Announcement.query.get(announcementId)
		assert a
	except:
		return {}, 404

	db.session.delete(a)
	db.session.commit()

	return {}, 200

