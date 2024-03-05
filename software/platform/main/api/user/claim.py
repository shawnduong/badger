from app import *
from flask_login import current_user, login_required

import json
import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/claim", methods=["GET"])
@login_required
@failsafe_500
def user_claim_get():
	r = requests.get(IMPLEMENTATION["user"]+f"/claim/{current_user.id}")
	return r.content, r.status_code

@app.route(userPrefix+f"/claim/<rewardId>", methods=["POST"])
@login_required
@failsafe_500
def user_claim_post(rewardId: int):

	# Make sure that the user has enough points for the reward they want.
	r = requests.get(IMPLEMENTATION["manage"]+f"/reward/{rewardId}")
	if r.status_code != 200:
		return {}, 404

	if current_user.update_points() - json.loads(r.content)["points"] >= 0:
		r = requests.post(IMPLEMENTATION["user"]+f"/claim/{rewardId}/{current_user.id}")
		return r.content, r.status_code

	return {"message": "Insufficient points balance."}, 400

