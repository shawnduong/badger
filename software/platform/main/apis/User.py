import requests

from app import *

from flask_login import current_user, login_required

userPrefix = "/api/v1/user"

#@app.route(prefix+"/user", methods=["GET"])
#@login_required
#def user_get():
#	r = requests.get(IMPLEMENTATION["user"]+"/user", json=request.json)
#	return r.content, r.status_code

@app.route(userPrefix+"/user", methods=["POST"])
def user_user_post():
	"""
	Set up a user account with required information. This is different than
	the POST user method under the Admin endpoint. Admin's will make the
	account, which must exist before the user adds their info to it using
	this method here.
	"""

	try:
		# These are required fields for this method.
		for k in ("uid", "email", "password", "custom"):
			assert k in request.form.keys()
	except:
		return {}, 400

	try:
		user = User.query.filter_by(uid=int(request.form["uid"])).all()

		# User must exist.
		if len(user) == 0:
			return {}, 400

		# There must not be more than one user.
		if len(user) > 1:
			return {}, 500

		user = user[0]

		# Account must not already be claimed.
		if user.claimed:
			return {}, 409

	except:
		return {}, 500

	try:
		user.claim(
			request.form["email"],
			request.form["password"],
			request.form["custom"]
		)
		db.session.commit()
		return {}, 201
	except:
		return {}, 400

	return {}, 500
