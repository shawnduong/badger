from app import *
from flask_login import current_user, login_required

import requests

publicPrefix = "/api/v1/public"

@app.route(publicPrefix+"/reset", methods=["POST"])
def public_reset_post():
	r = requests.post(IMPLEMENTATION["public"]+"/reset", json=request.json)
	return r.content, r.status_code

