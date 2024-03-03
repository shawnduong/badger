from app import *
from flask_login import current_user, login_required

import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/rsvp", methods=["GET"])
@login_required
@failsafe_500
def user_rsvp_get():
	r = requests.get(IMPLEMENTATION["user"]+f"/rsvp/{current_user.id}")
	return r.content, r.status_code

