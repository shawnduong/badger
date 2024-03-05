from app import *

import json
import requests
import time

@app.route(API+"/scan", methods=["POST"])
@failsafe_500
def scan_post():

	try:
		# These are required fields for this method.
		for k in ("authorization", "scannerId", "scans"):
			assert k in request.json.keys()
		scannerId = int(request.json["scannerId"])
		scans = json.loads(request.json["scans"])
	except:
		return {}, 400

	# Get the authorization from the configuration.
	r = requests.get(IMPLEMENTATION["admin"]+f"/configure/lookup/{scannerId}")
	if r.status_code != 200:
		return {}, 500

	data = json.loads(r.content)

	# Make sure the authorization is valid.
	try:
		assert data["authorization"] == request.json["authorization"]
	except:
		return {}, 401

	try:
		assert (s:=Scanner.query.filter_by(scannerId=scannerId).first())
	except:
		return {}, 404

	s.lastAlive = int(time.time())

	# TODO apply the scans.

	return {}, 202

