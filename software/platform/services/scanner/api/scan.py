from app import *

import json

@app.route(API+"/scan", methods=["POST"])
@failsafe_500
def scan_post():

	try:
		# These are required fields for this method.
		for k in ("authorization", "scannerId", "scans"):
			assert k in request.json.keys()
	except:
		return {}, 400

	# TODO

	return {}, 202

