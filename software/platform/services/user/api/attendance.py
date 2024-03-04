from app import *

import requests

@app.route(API+"/attendance/<userId>", methods=["GET"])
@failsafe_500
# nodoc
def attendance_get(userId: int):
	r = requests.get(IMPLEMENTATION["manage"]+f"/attendance/lookup/{userId}")
	return r.content, r.status_code

@app.route(API+"/attendance/<code>/<userId>", methods=["POST"])
@failsafe_500
# nodoc
def attendance_post(code: str, userId: int):

	# Find the event.
	try:
		r = requests.get(IMPLEMENTATION["manage"]+f"/event/lookup/{code}")
		assert r.status_code == 200
		userId = int(userId)
		eventId = int(json.loads(r.content)["id"])
	except:
		return r.content, r.status_code

	try:
		r = requests.post(IMPLEMENTATION["manage"]+"/attendance", json={
			"userId": userId, "eventId": eventId
		})
		assert r.status_code == 201
		return {}, 201
	except:
		pass

	return r.content, r.status_code

