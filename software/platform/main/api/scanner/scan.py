from app import *

import json
import requests

scannerPrefix = "/api/v1/scanner"

@app.route(scannerPrefix+"/scan", methods=["POST"])
@failsafe_500
def scanner_scan_post():
	r = requests.post(IMPLEMENTATION["scanner"]+"/scan", json=request.json)
	return r.content, r.status_code

