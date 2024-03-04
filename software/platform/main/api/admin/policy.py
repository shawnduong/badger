from app import *
from flask_login import current_user, login_required

import requests

adminPrefix = "/api/v1/admin"

@app.route(adminPrefix+"/policy", methods=["GET"])
@admin_required
@failsafe_500
def admin_policy_get():
	r = requests.get(IMPLEMENTATION["admin"]+"/policy")
	return r.content, r.status_code

@app.route(adminPrefix+"/policy", methods=["PATCH"])
@admin_required
@failsafe_500
def admin_policy_patch():
	r = requests.patch(IMPLEMENTATION["admin"]+"/policy", json=request.json)
	return r.content, r.status_code

