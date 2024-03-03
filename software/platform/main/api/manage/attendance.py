from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/attendance", methods=["GET"])
@admin_required
@failsafe_500
def manage_attendance_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/attendance")
	return r.content, r.status_code

@app.route(managePrefix+"/attendance", methods=["POST"])
@admin_required
@failsafe_500
def manage_attendance_post():

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

	r = requests.post(IMPLEMENTATION["manage"]+"/attendance", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/attendance/<attendanceId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_attendance_patch(attendanceId: int):

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

	r = requests.patch(IMPLEMENTATION["manage"]+f"/attendance/{attendanceId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/attendance/<attendanceId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_attendance_delete(attendanceId: int):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/attendance/{attendanceId}")
	return r.content, r.status_code

