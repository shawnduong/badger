from app import *

import requests

@app.route(API+"/event", methods=["GET"])
@failsafe_500
def event_get():

	r = requests.get(IMPLEMENTATION["manage"]+"/event")
	return r.content, r.status_code

