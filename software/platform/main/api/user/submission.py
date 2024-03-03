from app import *
from flask_login import current_user, login_required

import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/submission/<code>", methods=["POST"])
@login_required
@failsafe_500
def user_submission_post(code: str):

	r = requests.post(IMPLEMENTATION["user"]+f"/submission/{code}/{current_user.id}")
	return r.content, r.status_code

