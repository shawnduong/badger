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

	# TODO

	return {}, 202

