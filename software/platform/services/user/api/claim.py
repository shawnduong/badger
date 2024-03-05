from app import *

import requests

@app.route(API+"/claim/<userId>", methods=["GET"])
@failsafe_500
# nodoc
def claim_get(userId: int):
	r = requests.get(IMPLEMENTATION["manage"]+f"/claim/lookup/{userId}")
	return r.content, r.status_code

@app.route(API+"/claim/<rewardId>/<userId>", methods=["POST"])
@failsafe_500
# nodoc
def claim_post(rewardId: int, userId: int):
	r = requests.post(IMPLEMENTATION["manage"]+f"/claim", json={
		"rewardId": rewardId,
		"userId": userId,
		"retrieved": False
	})
	return r.content, r.status_code

