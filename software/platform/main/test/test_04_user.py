import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

admin = requests.Session()
admin.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

user = requests.Session()
user.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ GET YOUR OWN USER ACCOUNT DETAILS ]--

def test_user_user_get_200():

	r = user.get(API+"/user/user")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data == {
		"claimed": True,
		"email": "test@example.com",
		"id": 2,
		"points": 0,
		"uid": 0xf00df00d,
	}

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

	r = user.get(API+"/user/user")
	assert r.status_code == 200
	data = json.loads(r.content)
	assert data["points"] == 10

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

# --[ MAKE AN RSVP ]--

# Success.
def test_user_rsvp_post_201():
	r = user.post(API+"/user/rsvp/1")
	assert r.status_code == 201

# Not logged in.
def test_user_rsvp_post_302():
	r = requests.post(API+"/user/rsvp/1", allow_redirects=False)
	assert r.status_code == 302

# Bad form.
def test_user_rsvp_post_400():
	r = user.post(API+"/user/rsvp/abc")
	assert r.status_code == 400

# Event not found.
def test_user_rsvp_post_404():
	r = user.post(API+"/user/rsvp/999")
	assert r.status_code == 404

# RSVP already exists.
def test_user_rsvp_post_409():
	r = user.post(API+"/user/rsvp/1")
	assert r.status_code == 409

# --[ GET YOUR RSVPS ]--

# Success.
def test_user_rsvp_get_200():
	r = user.get(API+"/user/rsvp")
	assert r.status_code == 200
	assert json.loads(r.content) == [1]

# Not logged in.
def test_user_rsvp_get_302():
	r = requests.get(API+"/user/rsvp", allow_redirects=False)
	assert r.status_code == 302

# --[ DELETE AN RSVP ]--

# Success.
def test_user_rsvp_delete_200():
	r = user.delete(API+"/user/rsvp/1")
	assert r.status_code == 200

# Not logged in.
def test_user_rsvp_delete_302():
	r = requests.delete(API+"/user/rsvp/1", allow_redirects=False)
	assert r.status_code == 302

# Bad form.
def test_user_rsvp_delete_400():
	r = user.delete(API+"/user/rsvp/abc")
	assert r.status_code == 400

# RSVP for an event not found.
def test_user_rsvp_delete_404():
	r = user.delete(API+"/user/rsvp/1")
	assert r.status_code == 404

# --[ SUBMIT AN ATTENDANCE CODE ]--

# Success.
def test_user_attendance_post_201():

	# Make an event to attend.
	r = admin.post(API+"/manage/event", json={
		"title": "Billy Bob's Event",
		"location": "Room C1",
		"map": None,
		"startTime": 1708743600+3600*2,
		"duration": 3600,
		"code": "BILLY-BOB-1234",
		"points": 50,
		"host": "Billy Bob",
		"description": "Lorem ipsum dolor sit amet."
	})
	assert r.status_code == 201

	# Submit the attendance code.
	r = user.post(API+"/user/attendance/BILLY-BOB-1234")
	assert r.status_code == 201

	r = user.get(API+"/user/user")
	assert r.status_code == 200
	data = json.loads(r.content)
	assert data["points"] == 60

# Not logged in.
def test_user_attendance_post_302():
	r = requests.post(API+"/user/attendance/BILLY-BOB-1234", allow_redirects=False)
	assert r.status_code == 302

# Code not found.
def test_user_attendance_post_404():
	r = user.post(API+"/user/attendance/00000-111-2222")
	assert r.status_code == 404

# Submission already exists.
def test_user_attendance_post_409():
	r = user.post(API+"/user/attendance/BILLY-BOB-1234")
	assert r.status_code == 409

# --[ GET YOUR ATTENDANCES ]--

# Success.
def test_user_attendance_get_200():

	r = user.get(API+"/user/attendance")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert len(data) > 0

# Not logged in.
def test_user_attendance_get_302():
	r = requests.get(API+"/user/attendance", allow_redirects=False)
	assert r.status_code == 302

# --[ GET ALL ENTITLEMENTS ]--

# Success.
def test_user_entitlement_get_200():

	# Make some entitlements to get.
	r = admin.post(API+"/manage/entitlement", json={
		"title": "Breakfast",
		"quantity": 3
	})
	assert r.status_code == 201
	r = admin.post(API+"/manage/entitlement", json={
		"title": "Lunch",
		"quantity": 3
	})
	assert r.status_code == 201

	r = user.get(API+"/user/entitlement")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert len(data) == 2
	assert data[0]["title"] == "Breakfast"
	assert data[0]["quantity"] == 3
	assert data[0]["id"] == 1
	assert data[1]["title"] == "Lunch"
	assert data[1]["quantity"] == 3
	assert data[1]["id"] == 2

# Not logged in.
def test_user_entitlement_get_302():
	r = requests.get(API+"/user/entitlement", allow_redirects=False)
	assert r.status_code == 302

# --[ GET YOUR REDEMPTIONS ]--

# Success.
def test_user_redemption_get_200():

	# We need some redemptions first.
	r = admin.post(API+"/manage/redemption", json={
		"entitlementId": 1,
		"userId": 2
	})
	assert r.status_code == 201
	r = admin.post(API+"/manage/redemption", json={
		"entitlementId": 1,
		"userId": 2
	})
	assert r.status_code == 201
	r = admin.post(API+"/manage/redemption", json={
		"entitlementId": 2,
		"userId": 2
	})
	assert r.status_code == 201

	# Get your own redemptions.
	r = user.get(API+"/user/redemption")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data == [
		{"entitlementId": 1, "userId": 2, "id": 1},
		{"entitlementId": 1, "userId": 2, "id": 2},
		{"entitlementId": 2, "userId": 2, "id": 3},
	]

# Not logged in.
def test_user_redemption_get_302():
	r = requests.get(API+"/user/redemption", allow_redirects=False)
	assert r.status_code == 302

# --[ LIST THE REWARDS ]--

# Success.
def test_user_reward_get_200():

	r = user.get(API+"/user/reward")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data == [
		{
			"item": "Sticker Pack",
			"points": 50,
			"stockTotal": 150,
			"stockRemaining": 150,
			"id": 1,
		},
		{
			"item": "Electronics Kit",
			"points": 50,
			"stockTotal": 100,
			"stockRemaining": 100,
			"id": 2,
		},
	]

# Not logged in.
def test_user_reward_get_302():
	r = requests.get(API+"/user/reward", allow_redirects=False)
	assert r.status_code == 302

# --[ CLAIM A REWARD ]--

# Success.
def test_user_reward_post_200():
	r = user.post(API+"/user/claim/1")
	assert r.status_code == 201

# Not logged in.
def test_user_reward_post_302():
	r = requests.post(API+"/user/claim/1", allow_redirects=False)
	assert r.status_code == 302

# Not enough points.
def test_user_reward_post_400():
	r = user.post(API+"/user/claim/1")
	assert r.status_code == 400
	assert json.loads(r.content)["message"] == "Insufficient points balance."

# Reward not found.
def test_user_reward_post_404():
	r = user.post(API+"/user/claim/999")
	assert r.status_code == 404

