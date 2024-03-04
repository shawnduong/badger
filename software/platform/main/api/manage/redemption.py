from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/redemption", methods=["GET"])
@admin_required
@failsafe_500
def manage_redemption_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/redemption")
	return r.content, r.status_code

@app.route(managePrefix+"/redemption", methods=["POST"])
@admin_required
@failsafe_500
def manage_redemption_post():

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

	r = requests.post(IMPLEMENTATION["manage"]+"/redemption", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/redemption/<redemptionId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_redemption_patch(redemptionId: int):

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

	r = requests.patch(IMPLEMENTATION["manage"]+f"/redemption/{redemptionId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/redemption/<redemptionId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_redemption_delete(redemptionId: int):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/redemption/{redemptionId}")
	return r.content, r.status_code

