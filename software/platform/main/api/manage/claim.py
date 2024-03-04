from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/claim", methods=["GET"])
@admin_required
@failsafe_500
def manage_claim_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/claim")
	return r.content, r.status_code

@app.route(managePrefix+"/claim", methods=["POST"])
@admin_required
@failsafe_500
def manage_claim_post():

	# User ID is required.
	try:
		assert "userId" in request.json.keys()
		userId = int(request.json["userId"])
	except:
		return {}, 400

	# User must exist.
	try:
		assert User.query.get(userId)
	except:
		return {}, 404

	r = requests.post(IMPLEMENTATION["manage"]+"/claim", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/claim/<claimId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_claim_patch(claimId: int):

	# User ID is required.
	try:
		assert "userId" in request.json.keys()
		userId = int(request.json["userId"])
	except:
		return {}, 400

	# User must exist.
	try:
		assert User.query.get(userId)
	except:
		return {}, 404

	r = requests.patch(IMPLEMENTATION["manage"]+f"/claim/{claimId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/claim/<claimId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_claim_delete(claimId: int):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/claim/{claimId}")
	return r.content, r.status_code

