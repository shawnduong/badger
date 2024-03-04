from app import *
from flask_login import current_user, login_required

import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/reward", methods=["GET"])
@login_required
@failsafe_500
def user_reward_get():
	r = requests.get(IMPLEMENTATION["user"]+"/reward")
	return r.content, r.status_code

