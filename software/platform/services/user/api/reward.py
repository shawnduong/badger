from app import *

import requests

@app.route(API+"/reward", methods=["GET"])
@failsafe_500
def reward_get():
	r = requests.get(IMPLEMENTATION["manage"]+"/reward")
	return r.content, r.status_code

