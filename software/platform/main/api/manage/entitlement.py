from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/entitlement", methods=["POST"])
@admin_required
@failsafe_500
def manage_entitlement_post():
	r = requests.post(IMPLEMENTATION["manage"]+"/entitlement", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/entitlement/<entitlementId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_entitlement_patch(entitlementId: int):
	r = requests.patch(IMPLEMENTATION["manage"]+f"/entitlement/{entitlementId}", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/entitlement/<entitlementId>", methods=["DELETE"])
@admin_required
@failsafe_500
def manage_entitlement_delete(entitlementId: int):
	r = requests.delete(IMPLEMENTATION["manage"]+f"/entitlement/{entitlementId}")
	return r.content, r.status_code

