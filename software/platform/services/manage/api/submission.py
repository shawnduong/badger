from app import *

import requests
import json
import re

@app.route(API+"/submission", methods=["GET"])
@failsafe_500
def submission_get():

	submissions = [str(s) for s in Submission.query.all()]
	return submissions, 200

@app.route(API+"/submission", methods=["POST"])
@failsafe_500
def submission_post():

	try:
		# These are required fields for this method.
		for k in ("codeId", "userId"):
			assert k in request.json.keys()
		int(request.json["codeId"])
		int(request.json["userId"])
	except:
		return {}, 400

	# It is the responsibility of the caller to make sure that the code user
	# exists.

	db.session.add(Submission(int(request.json["codeId"]), int(request.json["userId"])))
	db.session.commit()

	return {}, 201

