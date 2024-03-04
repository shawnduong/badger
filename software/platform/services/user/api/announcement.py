from app import *

import requests

@app.route(API+"/announcement", methods=["GET"])
@failsafe_500
def announcement_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/announcement")
	return r.content, r.status_code

