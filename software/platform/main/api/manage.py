from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/code", methods=["GET"])
@admin_required
@failsafe_500
def manage_code_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/code")
	return r.content, r.status_code

@app.route(managePrefix+"/code", methods=["POST"])
@admin_required
@failsafe_500
def manage_code_post():
	r = requests.post(IMPLEMENTATION["manage"]+"/code", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/code/<codeId>", methods=["GET"])
@admin_required
@failsafe_500
def manage_code_get_specific(codeId: int):
	r = requests.get(IMPLEMENTATION["manage"]+f"/code/{codeId}")
	return r.content, r.status_code

@app.route(managePrefix+"/code/<codeId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_code_patch(codeId: int):
	r = requests.patch(IMPLEMENTATION["manage"]+f"/code/{codeId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/code/<codeId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_code_delete(codeId: int):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/code/{codeId}")
	return r.content, r.status_code

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
	except:
		return {}, 400

	try:
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
	except:
		return {}, 400

	try:
		userId = int(request.json["userId"])
		submissionId = int(submissionId)
	except:
		return {}, 400

	# User must exist.
	try:
		assert User.query.get(userId)
	except:
		return {}, 404

	r = requests.patch(IMPLEMENTATION["manage"]+f"/submission/{submissionId}", json=request.json)
	return r.content, r.status_code

