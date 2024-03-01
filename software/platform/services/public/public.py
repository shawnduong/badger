from app import *

import json
import re

API = "/api/v1/public"

def _valid_email(email: str):
	"""
	Return true if a possible email address string is valid. Credits to
	https://uibakery.io/regex-library/email-regex-python for the regex.
	"""

	pattern = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
	return re.match(pattern, email)

@app.route(API+"/reset", methods=["POST"])
@failsafe_500
def reset_post():
	data = json.loads(request.json)
	if "email" not in data.keys():
		return {}, 400
	if not _valid_email(data["email"]):
		return {}, 400
	# TODO: implement reset email.
	return {}, 202

