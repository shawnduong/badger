from app import *
from flask_login import current_user, login_required

import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/attendance", methods=["GET"])
@login_required
@failsafe_500
def user_attendance_get():
	r = requests.get(IMPLEMENTATION["user"]+f"/attendance/{current_user.id}")
	return r.content, r.status_code

@app.route(userPrefix+"/attendance/<code>", methods=["POST"])
@login_required
@failsafe_500
def user_attendance_post(code: str):
	r = requests.post(IMPLEMENTATION["user"]+f"/attendance/{code}/{current_user.id}")
	return r.content, r.status_code

