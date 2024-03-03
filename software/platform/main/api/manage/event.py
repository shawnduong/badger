from app import *
from flask_login import current_user, login_required

import requests

managePrefix = "/api/v1/manage"

@app.route(managePrefix+"/event", methods=["POST"])
@admin_required
@failsafe_500
def manage_event_post():
	r = requests.post(IMPLEMENTATION["manage"]+"/event", json=request.json)
	return r.content, r.status_code

@app.route(managePrefix+"/event/<eventId>", methods=["PATCH"])
@admin_required
@failsafe_500
def manage_event_patch(eventId: int):
	r = requests.patch(IMPLEMENTATION["manage"]+f"/event/{eventId}", json=request.json)
	return r.content, r.status_code

