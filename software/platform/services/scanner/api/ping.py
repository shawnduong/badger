from app import *

import json

@app.route(API+"/ping", methods=["POST"])
@failsafe_500
def ping_post():

	try:
		# These are required fields for this method.
		for k in ("authorization", "scannerId"):
			assert k in request.json.keys()
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

	return {}, 202

