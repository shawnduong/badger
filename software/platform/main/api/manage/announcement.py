from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/announcement", methods=["POST"])
@admin_required
@failsafe_500
def manage_announcement_post():
	r = requests.post(IMPLEMENTATION["manage"]+"/announcement", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/announcement/<announcementId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_announcement_patch(announcementId: int):
	r = requests.patch(IMPLEMENTATION["manage"]+f"/announcement/{announcementId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/announcement/<announcementId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_announcement_delete(announcementId: int):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/announcement/{announcementId}")
	return r.content, r.status_code

