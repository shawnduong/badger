from app import *
from flask_login import current_user, login_required

import requests

adminPrefix = "/api/v1/admin"

@app.route(adminPrefix+"/user", methods=["GET"])
@admin_required
@failsafe_500
def admin_user_get():

	users = User.query.all()
	output = [str(u) for u in users]

	return output, 200

@app.route(adminPrefix+"/user", methods=["POST"])
@admin_required
@failsafe_500
def admin_user_post():
	"""
	Create a user account. This is different than User's POST user method,
	which fills out the information in the account made here.
	"""

	try:
		# These are required fields for this method.
		for k in ("uid", "email", "points", "claimed", "custom", "privilege"):
			assert k in request.json.keys()
	except:
		return {}, 400

	try:
		assert User.query.filter_by(uid=request.json["uid"]).first() == None
	except:
		return {}, 409

	user = User(
		uid=request.json["uid"],
		privilege=request.json["privilege"],
		email=request.json["email"],
		points=request.json["points"],
		claimed=request.json["claimed"],
		custom=request.json["custom"],
	)
	db.session.add(user)
	db.session.commit()
	return {}, 201

@app.route(adminPrefix+"/user/<userId>", methods=["GET"])
@admin_required
@failsafe_500
def admin_user_get_specific(userId: int):

	try:
		int(userId)
	except:
		return {}, 400

	try:
		assert (u:=User.query.get(userId))
	except:
		return {}, 404

	return str(u), 200

@app.route(adminPrefix+"/user/<userId>", methods=["PATCH"])
@admin_required
@failsafe_500
def admin_user_patch(userId: int):

	try:
		# These are required fields for this method.
		for k in ("uid", "email", "points", "claimed", "custom", "privilege"):
			assert k in request.json.keys()
	except:
		return {}, 400

	try:
		assert (u:=User.query.get(userId))
	except:
		return {}, 404

	u.uid        = request.json["uid"]
	u.privilege  = request.json["privilege"]
	u.email      = request.json["email"]
	u.points     = request.json["points"]
	u.claimed    = request.json["claimed"]
	u.custom     = request.json["custom"]

	db.session.commit()
	return {}, 200

@app.route(adminPrefix+"/user/<userId>", methods=["DELETE"])
@admin_required
@failsafe_500
def admin_user_delete(userId: int):

	try:
		user = User.query.filter_by(id=userId).first()
		assert user != None
	except:
		return {}, 404

	db.session.delete(user)
	db.session.commit()
	return {}, 200

