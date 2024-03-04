from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/reward", methods=["POST"])
@admin_required
@failsafe_500
def manage_reward_post():
	r = requests.post(IMPLEMENTATION["manage"]+"/reward", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/reward/<rewardId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_reward_patch(rewardId: int):
	r = requests.patch(IMPLEMENTATION["manage"]+f"/reward/{rewardId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/reward/<rewardId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_reward_delete(rewardId: int):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/reward/{rewardId}")
	return r.content, r.status_code

