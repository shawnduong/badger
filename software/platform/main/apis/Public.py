import requests

from app import *

from flask_login import current_user, login_required

class Public:

	prefix = "/api/v1/public"

	@app.route(prefix+"/reset", methods=["POST"])
	def reset_post():
		# Stub.
		r = requests.post(IMPLEMENTATION["public"]+"/reset", json=request.json)
		return r.content, r.status_code

