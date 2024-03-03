import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

admin = requests.Session()
admin.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

user = requests.Session()
user.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ MAKE A CODE ]--

# Success.
def test_manage_code_post_201():
	r = admin.post(API+"/manage/code", json={
		"code": "AAAA-BB-CCCC",
		"points": 100
	})
	assert r.status_code == 201

# Bad form.
def test_manage_code_post_400():
	r = admin.post(API+"/manage/code", json={
		"code": "AAAA-BB-CCCC",
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_code_post_401():
	r = user.post(API+"/manage/code", json={
		"code": "2222-11-0000",
		"points": 50
	})
	assert r.status_code == 401

# Code already exists.
def test_manage_code_post_409():
	r = admin.post(API+"/manage/code", json={
		"code": "AAAA-BB-CCCC",
		"points": 100
	})
	assert r.status_code == 409

# --[ GET CODES ]--

# Success.
def test_manage_code_get_200():

	r = admin.get(API+"/manage/code")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["code"] == "AAAA-BB-CCCC"
	assert data[0]["points"] == 100
	assert data[0]["id"] == 1

# Bad permissions.
def test_manage_code_get_401():

	r = user.get(API+"/manage/code")
	assert r.status_code == 401

# --[ GET A SPECIFIC CODE ]--

# Success.
def test_manage_code_get_specific_200():

	r = admin.get(API+"/manage/code/1")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["code"] == "AAAA-BB-CCCC"
	assert data["points"] == 100
	assert data["id"] == 1

# Bad form.
def test_manage_code_get_specific_400():
	r = admin.get(API+"/manage/code/abc")
	assert r.status_code == 400

# Bad permissions.
def test_manage_code_get_specific_401():
	r = user.get(API+"/manage/code/1")
	assert r.status_code == 401

# Code doesn't exist.
def test_manage_code_get_specific_404():
	r = admin.get(API+"/manage/code/999")
	assert r.status_code == 404

# --[ CHANGE INFO ABOUT A CODE ]--

# Success.
def test_manage_code_patch_200():

	r = admin.patch(API+"/manage/code/1", json={
		"code": "AAAA-BB-CCCC",
		"points": 250
	})
	assert r.status_code == 200

	r = admin.get(API+"/manage/code")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["code"] == "AAAA-BB-CCCC"
	assert data[0]["points"] == 250
	assert data[0]["id"] == 1

# Bad form.
def test_manage_code_patch_400():
	r = admin.patch(API+"/manage/code/1", json={
		"code": "AAAA-BB-CCCC",
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_code_patch_401():

	r = user.patch(API+"/manage/code/1", json={
		"code": "AAAA-BB-CCCC",
		"points": 999
	})
	assert r.status_code == 401

# Code doesn't exist.
def test_manage_code_patch_404():
	r = admin.patch(API+"/manage/code/9999", json={
		"code": "AAAA-BB-CCCC",
		"points": 250
	})
	assert r.status_code == 404

# --[ DELETE A CODE ]--

# Success.
def test_manage_code_delete_200():
	r = admin.delete(API+"/manage/code/1")
	assert r.status_code == 200

	r = admin.delete(API+"/manage/code/1")
	assert r.status_code == 404

# Bad permissions.
def test_manage_code_delete_401():
	r = user.delete(API+"/manage/code/1")
	assert r.status_code == 401

# Code doesn't exist.
def test_manage_code_delete_404():
	r = admin.delete(API+"/manage/code/999")
	assert r.status_code == 404

# --[ SUBMIT A CODE ON BEHALF OF A USER ]--

# Success.
def test_manage_submission_post_201():

	# Make a code for testing. ID 1.
	r = admin.post(API+"/manage/code", json={
		"code": "FOO-BAR-123",
		"points": 200
	})
	assert r.status_code == 201

	# Make sure that was ID 1.
	r = admin.get(API+"/manage/code/1")
	data = json.loads(r.content)
	assert data["id"] == 1

	# Make another code for testing. ID 2.
	r = admin.post(API+"/manage/code", json={
		"code": "FOO-BAR-321",
		"points": 200
	})
	assert r.status_code == 201

	# Submit the code for another user.
	r = admin.post(API+"/manage/submission", json={
		"codeId": 1,
		"userId": 2,
	})
	assert r.status_code == 201

# Bad form.
def test_manage_submission_post_400():
	r = admin.post(API+"/manage/submission", json={
		"userId": 2,
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_submission_post_401():

	# Submit the code for another user.
	r = user.post(API+"/manage/submission", json={
		"codeId": 1,
		"userId": 2,
	})
	assert r.status_code == 401

# Code doesn't exist.
def test_manage_submission_post_404_0():
	r = admin.post(API+"/manage/submission", json={
		"codeId": 999,
		"userId": 2,
	})
	assert r.status_code == 404

# User doesn't exist.
def test_manage_submission_post_404_1():
	r = admin.post(API+"/manage/submission", json={
		"codeId": 2,
		"userId": 999,
	})
	assert r.status_code == 404

# Submission already exists.
def test_manage_submission_post_409():
	r = admin.post(API+"/manage/submission", json={
		"codeId": 1,
		"userId": 2,
	})
	assert r.status_code == 409

# --[ GET ALL SUBMISSIONS ]--

# Success.
def test_manage_submission_get_200():
	r = admin.get(API+"/manage/submission")
	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["codeId"] == 1
	assert data[0]["userId"] == 2
	assert data[0]["id"] == 1

# Bad permissions.
def test_manage_submission_get_401():
	r = user.get(API+"/manage/submission")
	assert r.status_code == 401

# --[ EDIT A SUBMISSION ]--

# Success.
def test_manage_submission_patch_200():
	r = admin.patch(API+"/manage/submission/1", json={
		"codeId": 2,
		"userId": 1,
	})
	assert r.status_code == 200

# Bad form.
def test_manage_submission_patch_400():
	r = admin.patch(API+"/manage/submission/1", json={
		"userId": 2,
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_submission_patch_401():
	r = user.patch(API+"/manage/submission/1", json={
		"codeId": 2,
		"userId": 2,
	})
	assert r.status_code == 401

# Code not found.
def test_manage_submission_patch_404_0():
	r = admin.patch(API+"/manage/submission/1", json={
		"codeId": 999,
		"userId": 2,
	})
	assert r.status_code == 404

# User not found.
def test_manage_submission_patch_404_1():
	r = admin.patch(API+"/manage/submission/1", json={
		"codeId": 2,
		"userId": 999,
	})
	assert r.status_code == 404

# Submission not found.
def test_manage_submission_patch_404_1():
	r = admin.patch(API+"/manage/submission/999", json={
		"codeId": 2,
		"userId": 2,
	})
	assert r.status_code == 404

# --[ DELETE A SUBMISSION ]--

# Success.
def test_manage_submission_delete_200():
	r = admin.delete(API+"/manage/submission/1")
	assert r.status_code == 200

# Bad form.
def test_manage_submission_delete_400():
	r = admin.delete(API+"/manage/submission/abc")
	assert r.status_code == 400

# Bad permissions.
def test_manage_submission_delete_401():
	r = user.delete(API+"/manage/submission/1")
	assert r.status_code == 401


# Submission not found.
def test_manage_submission_delete_404():
	r = admin.delete(API+"/manage/submission/999")
	assert r.status_code == 404

# --[ POST AN ANNOUNCEMENT ]--

# Success.
def test_manage_announcement_post_201():
	r = admin.post(API+"/manage/announcement", json={
		"timestamp": 1708743600,
		"body": "We have leftover pizza in Room B4 if anyone would like to grab some!",
		"author": "Jane Doe"
	})
	assert r.status_code == 201

# Bad form.
def test_manage_announcement_post_400():
	r = admin.post(API+"/manage/announcement", json={
		"timestamp": 1708743600,
		"author": "Jane Doe"
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_announcement_post_401():
	r = user.post(API+"/manage/announcement", json={
		"timestamp": 1708743600,
		"body": "We have leftover pizza in Room B4 if anyone would like to grab some!",
		"author": "Jane Doe"
	})
	assert r.status_code == 401

# --[ GET ALL ANNOUNCEMENTS ]--

# Success.
def test_user_announcement_get_200():

	r = user.get(API+"/user/announcement")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["timestamp"] == 1708743600
	assert data[0]["body"] == "We have leftover pizza in Room B4 if anyone would like to grab some!"
	assert data[0]["author"] == "Jane Doe"
	assert data[0]["id"] == 1

# Not logged in.
def test_user_announcement_get_302():
	r = requests.get(API+"/user/announcement", allow_redirects=False)
	assert r.status_code == 302

# --[ UPDATE AN ANNOUNCEMENT ]--

# Success.
def test_manage_announcement_patch_200():

	r = admin.patch(API+"/manage/announcement/1", json={
		"timestamp": 1708743600,
		"body": "We have leftover pizza in Room A4 if anyone would like to grab some!",
		"author": "Jane Doe"
	})
	assert r.status_code == 200

	r = user.get(API+"/user/announcement")
	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["body"] == "We have leftover pizza in Room A4 if anyone would like to grab some!"

# Bad form.
def test_manage_announcement_patch_400():
	r = admin.patch(API+"/manage/announcement/1", json={
		"timestamp": 1708743600,
		"author": "Jane Doe"
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_announcement_patch_401():
	r = user.patch(API+"/manage/announcement/1", json={
		"timestamp": 1708743600,
		"body": "We have leftover pizza in Room A4 if anyone would like to grab some!",
		"author": "Jane Doe"
	})
	assert r.status_code == 401

# Not found.
def test_manage_announcement_patch_404():
	r = admin.patch(API+"/manage/announcement/999", json={
		"timestamp": 1708743600,
		"body": "We have leftover pizza in Room A4 if anyone would like to grab some!",
		"author": "Jane Doe"
	})
	assert r.status_code == 404

# --[ DELETE AN ANNOUNCEMENT ]--

# Success.
def test_manage_announcement_delete_200():
	r = admin.delete(API+"/manage/announcement/1")
	assert r.status_code == 200

# Bad permissions.
def test_manage_announcement_delete_401():
	r = user.delete(API+"/manage/announcement/1")
	assert r.status_code == 401

# Not found.
def test_manage_announcement_delete_404():
	r = admin.delete(API+"/manage/announcement/999")
	assert r.status_code == 404

# --[ POST AN EVENT ]--

# Success.
def test_manage_event_post_201():

	r = admin.post(API+"/manage/event", json={
		"title": "Opening Ceremony",
		"location": "Room A1",
		"map": None,
		"startTime": 1708743600,
		"duration": 3600,
		"points": 50,
		"host": "Jane Doe",
		"description": "Lorem ipsum dolor sit amet."
	})
	assert r.status_code == 201

	r = user.get(API+"/user/event")
	assert r.status_code == 200
	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["description"] == "Lorem ipsum dolor sit amet."

# Bad form.
def test_manage_event_post_400():
	r = admin.post(API+"/manage/event", json={
		"title": "Opening Ceremony",
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_event_post_401():
	r = user.post(API+"/manage/event", json={
		"title": "Opening Ceremony",
		"location": "Room A1",
		"map": None,
		"startTime": 1708743600,
		"duration": 3600,
		"points": 50,
		"host": "Jane Doe",
		"description": "Lorem ipsum dolor sit amet."
	})
	assert r.status_code == 401

# --[ UPDATE AN EVENT ]--

# Success.
def test_manage_event_patch_200():

	r = admin.patch(API+"/manage/event/1", json={
		"title": "Opening Ceremony",
		"location": "Room A1",
		"map": None,
		"startTime": 1708743600,
		"duration": 3600,
		"points": 50,
		"host": "Jane Doe",
		"description": "The quick brown fox jumps over the lazy dog."
	})
	assert r.status_code == 200

	r = user.get(API+"/user/event")
	assert r.status_code == 200
	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["description"] == "The quick brown fox jumps over the lazy dog."

# Bad form.
def test_manage_event_patch_400():
	r = admin.patch(API+"/manage/event/1", json={
		"title": "Opening Ceremony",
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_event_patch_401():
	r = user.patch(API+"/manage/event/1", json={
		"title": "Opening Ceremony",
		"location": "Room A1",
		"map": None,
		"startTime": 1708743600,
		"duration": 3600,
		"points": 50,
		"host": "Jane Doe",
		"description": "The quick brown fox jumps over the lazy dog."
	})
	assert r.status_code == 401

# --[ DELETE AN EVENT ]--

# Success.
def test_manage_event_delete_200():

	r = admin.delete(API+"/manage/event/1")
	assert r.status_code == 200

	r = user.get(API+"/user/event")
	assert r.status_code == 200
	assert len(json.loads(r.content)) == 0

# Unauthorized.
def test_manage_event_delete_401():
	r = user.delete(API+"/manage/event/1")
	assert r.status_code == 401

# Not found.
def test_manage_event_delete_404():
	r = admin.delete(API+"/manage/event/999")
	assert r.status_code == 404

# --[ CREATE AN RSVP ON BEHALF OF ANOTHER USER ]--

# Success.
def test_manage_rsvp_post_201():

	# Make an event to RSVP to.
	r = admin.post(API+"/manage/event", json={
		"title": "Opening Ceremony",
		"location": "Room A1",
		"map": None,
		"startTime": 1708743600,
		"duration": 3600,
		"points": 50,
		"host": "Jane Doe",
		"description": "Lorem ipsum dolor sit amet."
	})
	assert r.status_code == 201

	r = admin.post(API+"/manage/rsvp", json={
		"userId": 2,
		"eventId": 1
	})
	assert r.status_code == 201

# Bad form.
def test_manage_rsvp_post_400():
	r = admin.post(API+"/manage/rsvp", json={
		"userId": 2,
	})
	assert r.status_code == 400

# Unauthorized.
def test_manage_rsvp_post_400():
	r = user.post(API+"/manage/rsvp", json={
		"userId": 2,
		"eventId": 1
	})
	assert r.status_code == 401

# User not found.
def test_manage_rsvp_post_404_0():
	r = admin.post(API+"/manage/rsvp", json={
		"userId": 999,
		"eventId": 1
	})
	assert r.status_code == 404

# Event not found.
def test_manage_rsvp_post_404_1():
	r = admin.post(API+"/manage/rsvp", json={
		"userId": 1,
		"eventId": 999
	})
	assert r.status_code == 404

# RSVP already exists.
def test_manage_rsvp_post_409():
	r = admin.post(API+"/manage/rsvp", json={
		"userId": 2,
		"eventId": 1
	})
	assert r.status_code == 409

# --[ GET ALL RSVPS ]--

# Success.
def test_manage_rsvp_get_200():

	r = admin.get(API+"/manage/rsvp")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert len(data) > 0
	assert data[0]["userId"] == 2
	assert data[0]["eventId"] == 1

# Unauthorized.
def test_manage_rsvp_get_401():
	r = user.get(API+"/manage/rsvp")
	assert r.status_code == 401

# --[ UPDATE AN RSVP ]--

# Success.
def test_manage_rsvp_patch_200():

	# Make a new event for testing.
	r = admin.post(API+"/manage/event", json={
		"title": "Next Event",
		"location": "Room A1",
		"map": None,
		"startTime": 1708743600+3600,
		"duration": 3600,
		"points": 50,
		"host": "John Doe",
		"description": "Lorem ipsum dolor sit amet."
	})
	assert r.status_code == 201

	r = admin.patch(API+"/manage/rsvp/1", json={
		"userId": 2,
		"eventId": 2
	})
	assert r.status_code == 200

# Bad form.
def test_manage_rsvp_patch_400():
	r = admin.patch(API+"/manage/rsvp/1", json={
		"eventId": 2
	})
	assert r.status_code == 400

# Bad permissions.
def test_manage_rsvp_patch_401():
	r = user.patch(API+"/manage/rsvp/1", json={
		"userId": 2,
		"eventId": 2
	})
	assert r.status_code == 401

# RSVP not found.
def test_manage_rsvp_patch_404_0():
	r = admin.patch(API+"/manage/rsvp/999", json={
		"userId": 2,
		"eventId": 2
	})
	assert r.status_code == 404

# User not found.
def test_manage_rsvp_patch_404_1():
	r = admin.patch(API+"/manage/rsvp/1", json={
		"userId": 999,
		"eventId": 2
	})
	assert r.status_code == 404

# Event not found.
def test_manage_rsvp_patch_404_2():
	r = admin.patch(API+"/manage/rsvp/1", json={
		"userId": 2,
		"eventId": 999
	})
	assert r.status_code == 404

# RSVP already exists.
def test_manage_rsvp_patch_409():
	r = admin.patch(API+"/manage/rsvp/1", json={
		"userId": 2,
		"eventId": 2
	})
	assert r.status_code == 409

# --[ DELETE AN EVENT ]--

# Success.
def test_manage_rsvp_delete_200():
	r = admin.delete(API+"/manage/rsvp/1")
	assert r.status_code == 200

# Bad client form.
def test_manage_rsvp_delete_400():
	r = admin.delete(API+"/manage/rsvp/abc")
	assert r.status_code == 400

# Unauthorized.
def test_manage_rsvp_delete_401():
	r = user.delete(API+"/manage/rsvp/1")
	assert r.status_code == 401

# RSVP not found.
def test_manage_rsvp_delete_404():
	r = admin.delete(API+"/manage/rsvp/999")
	assert r.status_code == 404

