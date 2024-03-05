from app import *
from flask_login import current_user, login_required

import requests

adminPrefix = "/api/v1/admin"

@app.route(adminPrefix+"/configure", methods=["GET"])
@admin_required
@failsafe_500
def admin_configure_get():
	r = requests.get(IMPLEMENTATION["admin"]+"/configure")
	return r.content, r.status_code

@app.route(adminPrefix+"/configure", methods=["POST"])
@admin_required
@failsafe_500
def admin_configure_post():
	r = requests.post(IMPLEMENTATION["admin"]+"/configure", json=request.json)
	return r.content, r.status_code

@app.route(adminPrefix+"/configure/<configurationId>", methods=["PATCH"])
@admin_required
@failsafe_500
def admin_configure_patch(configurationId: int):
	r = requests.patch(IMPLEMENTATION["admin"]+f"/configure/{configurationId}", json=request.json)
	return r.content, r.status_code

@app.route(adminPrefix+"/configure/<configurationId>", methods=["DELETE"])
@admin_required
@failsafe_500
def admin_configure_delete(configurationId: int):
	r = requests.delete(IMPLEMENTATION["admin"]+f"/configure/{configurationId}")
	return r.content, r.status_code
