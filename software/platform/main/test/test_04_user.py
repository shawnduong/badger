import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

admin = requests.Session()
admin.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

user = requests.Session()
user.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ REDEEM A CODE ]--

# Success.
def test_user_submission_post_201():

	# Make a code for testing.
	r = admin.post(API+"/manage/code", json={
		"code": "HELLO-WORLD",
		"points": 10
	})
	assert r.status_code == 201

	r = user.post(API+"/user/submission/HELLO-WORLD")
	assert r.status_code == 201

# Not logged in.
def test_user_submission_post_302():
	r = requests.post(API+"/user/submission/HELLO-WORLD", allow_redirects=False)
	assert r.status_code == 302

# Invalid code.
def test_user_submission_post_404():
	r = user.post(API+"/user/submission/HELLO-WORLD123123")
	assert r.status_code == 404

# Already submitted.
def test_user_submission_post_409():
	r = user.post(API+"/user/submission/HELLO-WORLD")
	assert r.status_code == 409

# --[ GET YOUR RSVPS ]--

# Success.
def test_user_rsvp_get_200():
	pass
