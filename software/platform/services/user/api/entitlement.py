from app import *

import requests

@app.route(API+"/entitlement", methods=["GET"])
@failsafe_500
def entitlement_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/entitlement")
	return r.content, r.status_code

