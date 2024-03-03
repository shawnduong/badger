from app import *

import json
import requests

@app.route(API+"/submission/<code>/<userId>", methods=["POST"])
@failsafe_500
def submission_post(code: str, userId: int):

	r = requests.get(IMPLEMENTATION["manage"]+f"/code/lookup/{code}")

	if r.status_code != 200:
		return {}, r.status_code

	data = json.loads(r.content)
	r = requests.post(IMPLEMENTATION["manage"]+"/submission", json={
		"codeId": data["id"],
		"userId": userId
	})
	return r.content, r.status_code

