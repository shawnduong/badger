from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/submission", methods=["GET"])
@admin_required
@failsafe_500
def manage_submission_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/submission")
	return r.content, r.status_code

@app.route(managePrefix+"/submission", methods=["POST"])
@admin_required
@failsafe_500
def manage_submission_post():

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

	r = requests.post(IMPLEMENTATION["manage"]+"/submission", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/submission/<submissionId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_submission_patch(submissionId: int):

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

	r = requests.patch(IMPLEMENTATION["manage"]+f"/submission/{submissionId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/submission/<submissionId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_submission_delete(submissionId: int):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/submission/{submissionId}")
	return r.content, r.status_code

