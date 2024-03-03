from app import *

@app.route(API+"/attendance", methods=["GET"])
@failsafe_500
def attendance_get():

	attendances = [str(a) for a in Attendance.query.all()]
	return attendances, 200

@app.route(API+"/attendance", methods=["POST"])
@failsafe_500
def attendance_post():

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

	# Must be unique.
	try:
		assert not Attendance.query.filter_by(userId=userId, eventId=eventId).first()
	except:
		return {}, 409

	db.session.add(Attendance(userId, eventId))
	db.session.commit()
	return {}, 201

@app.route(API+"/attendance/<attendanceId>", methods=["PATCH"])
@failsafe_500
def attendance_patch(attendanceId: int):

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

	try:
		a = Attendance.query.get(attendanceId)
		assert a
	except:
		return {}, 404

	# Must be unique.
	try:
		assert not Attendance.query.filter_by(userId=userId, eventId=eventId).first()
	except:
		return {}, 409

	a.userId = userId
	a.eventId = eventId
	db.session.commit()

	return {}, 200

@app.route(API+"/attendance/<attendanceId>", methods=["DELETE"])
@failsafe_500
def attendance_delete(attendanceId: int):

	try:
		attendanceId = int(attendanceId)
	except:
		return {}, 400

	try:
		a = Attendance.query.get(attendanceId)
		assert a
	except:
		return {}, 404

	db.session.delete(a)
	db.session.commit()

	return {}, 200

