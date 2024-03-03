from app import *
from flask_login import current_user, login_required

import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/event", methods=["GET"])
@login_required
@failsafe_500
def user_event_get():

	r = requests.get(IMPLEMENTATION["user"]+"/event")
	return r.content, r.status_code


