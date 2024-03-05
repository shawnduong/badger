from app import *

import json
import requests

scannerPrefix = "/api/v1/scanner"

@app.route(scannerPrefix+"/ping", methods=["POST"])
@failsafe_500
def scanner_ping_post():
	r = requests.post(IMPLEMENTATION["scanner"]+"/ping", json=request.json)
	return r.content, r.status_code

