from app import *

import json
import re

API = "/api/v1/admin"

@app.route(API+"/policy", methods=["GET"])
@failsafe_500
def policy_get():

	policy = Policy.query.first()
	return str(policy), 200

@app.route(API+"/policy", methods=["PATCH"])
@failsafe_500
def policy_patch():

	try:
		# These are required fields for this method.
		for k in ("requireRegistration", "selfServiceAccountReset", "selfServiceAccountResetExpiry"):
			assert k in request.json.keys()
	except:
		return {}, 400

	policy = Policy.query.first()
	policy.requireRegistration            = request.json["requireRegistration"]
	policy.selfServiceAccountReset        = request.json["selfServiceAccountReset"]
	policy.selfServiceAccountResetExpiry  = request.json["selfServiceAccountResetExpiry"]
	db.session.commit()

	return {}, 200

