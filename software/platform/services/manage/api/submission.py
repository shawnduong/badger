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
		codeId = int(request.json["codeId"])
		userId = int(request.json["userId"])
	except:
		return {}, 400

	# It is the responsibility of the caller to make sure that the user exists
	# and return a 404 if not.
	try:
		r = requests.get(IMPLEMENTATION["manage"]+f"/code/{codeId}")
		assert r.status_code == 200
	except:
		return {}, r.status_code

	# This submission must be unique.
	try:
		s = Submission.query.filter_by(codeId=codeId, userId=userId).all()
		assert len(s) == 0
	except:
		return {}, 409

	db.session.add(Submission(codeId, userId))
	db.session.commit()

	return {}, 201

@app.route(API+"/submission/<submissionId>", methods=["PATCH"])
@failsafe_500
def submission_patch(submissionId: int):

	try:
		# These are required fields for this method.
		for k in ("codeId", "userId"):
			assert k in request.json.keys()
		codeId = int(request.json["codeId"])
		userId = int(request.json["userId"])
	except:
		return {}, 400

	# It is the responsibility of the caller to make sure that the user exists
	# and return a 404 if not.
	try:
		r = requests.get(IMPLEMENTATION["manage"]+f"/code/{codeId}")
		assert r.status_code == 200
	except:
		return {}, r.status_code

	# This submission's new info must be unique.
	try:
		s = Submission.query.filter_by(codeId=codeId, userId=userId).all()
		assert len(s) == 0
	except:
		return {}, 409

	# Get the existing submission.
	try:
		s = Submission.query.get(submissionId)
		assert s
	except:
		return {}, 404

	# Apply the changes.
	s.codeId = codeId
	s.userId = userId
	db.session.commit()

	return {}, 200
