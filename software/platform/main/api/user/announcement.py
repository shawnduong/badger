from app import *
from flask_login import current_user, login_required

import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/announcement", methods=["GET"])
@login_required
@failsafe_500
def user_announcement_get():
	r = requests.get(IMPLEMENTATION["user"]+"/announcement")
	return r.content, r.status_code

