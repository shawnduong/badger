from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/rsvp", methods=["GET"])
@admin_required
@failsafe_500
def manage_rsvp_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/rsvp")
	return r.content, r.status_code

@app.route(managePrefix+"/rsvp", methods=["POST"])
@admin_required
@failsafe_500
def manage_rsvp_post():

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

	r = requests.post(IMPLEMENTATION["manage"]+"/rsvp", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/rsvp/<rsvpId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_rsvp_patch(rsvpId: int):

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

	r = requests.patch(IMPLEMENTATION["manage"]+f"/rsvp/{rsvpId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/rsvp/<rsvpId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_rsvp_delete(rsvpId: int):

	r = requests.delete(IMPLEMENTATION["manage"]+f"/rsvp/{rsvpId}")
	return r.content, r.status_code

