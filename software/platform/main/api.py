from app import *

import requests
from flask_login import current_user, login_required

class Public:

	@app.route("/api/v1/public/reset", methods=["POST"])
	def reset_post():
		r = requests.post(IMPLEMENTATION["public"]+"/reset", json=request.json)
		return r.content, r.status_code

#class User:
#class Manage:
#class Admin:
#class Scanner:
