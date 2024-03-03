from app import *

import requests

@app.route(API+"/rsvp/<userId>", methods=["GET"])
@failsafe_500
def rsvp_get(userId: int):

	r = requests.get(IMPLEMENTATION["manage"]+f"/rsvp/lookup/{userId}")
	return r.content, r.status_code

