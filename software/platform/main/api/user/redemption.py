from app import *
from flask_login import current_user, login_required

import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/redemption", methods=["GET"])
@login_required
@failsafe_500
def user_redemption_get():
	r = requests.get(IMPLEMENTATION["user"]+f"/redemption/{current_user.id}")
	return r.content, r.status_code

