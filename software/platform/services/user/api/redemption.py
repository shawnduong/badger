from app import *

import requests

@app.route(API+"/redemption/<userId>", methods=["GET"])
@failsafe_500
# nodoc
def redemption_get(userId: int):
	r = requests.get(IMPLEMENTATION["manage"]+f"/redemption/lookup/{userId}")
	return r.content, r.status_code

