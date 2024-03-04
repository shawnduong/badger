from app import *
from flask_login import current_user, login_required

import requests

userPrefix = "/api/v1/user"

@app.route(userPrefix+"/entitlement", methods=["GET"])
@login_required
@failsafe_500
def admin_entitlement_get():
	r = requests.get(IMPLEMENTATION["user"]+"/entitlement")
	return r.content, r.status_code
