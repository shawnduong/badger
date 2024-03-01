import requests

from app import *

from flask_login import current_user, login_required

class Public:

	prefix = "/api/v1/public"

	@app.route(prefix+"/reset", methods=["POST"])
	def reset_post():
		r = requests.post(IMPLEMENTATION["public"]+"/reset", json=request.json)
		return r.content, r.status_code

class UserApi:
	"""
	The "Api" part is added to the name to prevent a namespace conflict with the
	User model.
	"""

	prefix = "/api/v1/user"

#	@app.route(prefix+"/user", methods=["GET"])
#	@login_required
#	def user_get():
#		r = requests.get(IMPLEMENTATION["user"]+"/user", json=request.json)
#		return r.content, r.status_code

	@app.route(prefix+"/user", methods=["POST"])
	def user_post():
		"""
		Create a user account. This is not a stub.
		"""

		try:
			assert "uid" in request.form.keys()
			assert "email" in request.form.keys()
			assert "password" in request.form.keys()
			assert "custom" in request.form.keys()
		except:
			return {}, 400

		try:
			uid = int(request.form["uid"])
			print(uid)
			user = User.query.filter_by(uid=uid).all()
			print(user)
			if len(user) == 0:
				return {}, 400
			if len(user) > 1:
				return {}, 500
			user = user[0]
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

#class Manage:
#class Admin:
#class Scanner:
