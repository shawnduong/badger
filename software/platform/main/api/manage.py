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

@app.route(managePrefix+"/code/<codeId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_code_patch(codeId):
	r = requests.patch(IMPLEMENTATION["manage"]+f"/code/{codeId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/code/<codeId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_code_delete(codeId):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/code/{codeId}")
	return r.content, r.status_code

