from app import *

import requests

@app.route(API+"/rsvp/<userId>", methods=["GET"])
@failsafe_500
# nodoc
def rsvp_get(userId: int):
	r = requests.get(IMPLEMENTATION["manage"]+f"/rsvp/lookup/{userId}")
	data = [json.loads(obj)["eventId"] for obj in json.loads(r.content)]
	return data, r.status_code

@app.route(API+"/rsvp/<eventId>/<userId>", methods=["POST"])
@failsafe_500
# nodoc
def rsvp_post(eventId: int, userId: int):

	try:
		userId = int(userId)
		eventId = int(eventId)
	except:
		return {}, 400

	r = requests.post(IMPLEMENTATION["manage"]+"/rsvp", json={
		"userId": userId, "eventId": eventId
	})
	return r.content, r.status_code

@app.route(API+"/rsvp/<eventId>/<userId>", methods=["DELETE"])
@failsafe_500
# nodoc
def rsvp_delete(eventId: int, userId: int):

	r = requests.get(IMPLEMENTATION["manage"]+f"/rsvp/lookup/{userId}")
	data = [json.loads(obj) for obj in json.loads(r.content)]

	try:
		userId = int(userId)
		eventId = int(eventId)
	except:
		return {}, 400

	for d in data:
		if d["eventId"] == eventId:
			r = requests.delete(IMPLEMENTATION["manage"]+f"/rsvp/{d['id']}")
			return r.content, r.status_code

	return {}, 404

