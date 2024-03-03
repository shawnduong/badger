import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

# Default admin login.
admin = requests.Session()
admin.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

# Make a default user account.
r = admin.post(API+"/admin/user", json={
	"uid": 0xf00df00d,
	"email": None,
	"points": None,
	"claimed": False,
	"custom": None,
	"privilege": 0
})
assert r.status_code == 201

# Claim the default user account.
r = requests.post(API+"/user/user", data={
	"uid": 0xf00df00d,
	"email": "user@test.com",
	"password": "user",
	"custom": "",
})
assert r.status_code == 201

# Test user login.
user = requests.Session()
user.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ MAKE AN ACCOUNT ]--

# Success.
def test_admin_user_post_201():
	r = admin.post(API+"/admin/user", json={
		"uid": 0xdeadbeef,
		"email": None,
		"points": None,
		"claimed": False,
		"custom": None,
		"privilege": 0
	})
	assert r.status_code == 201

# Bad form. Missing the email.
def test_admin_user_post_400():
	r = admin.post(API+"/admin/user", json={
		"uid": 0xdeadbeef,
		"points": None,
		"claimed": False,
		"custom": None,
		"privilege": 0
	})
	assert r.status_code == 400

# Bad permissions.
def test_admin_user_post_401():
	r = user.post(API+"/admin/user", json={
		"uid": 0xdeadbeef+1,
		"email": None,
		"points": None,
		"claimed": False,
		"custom": None,
		"privilege": 0
	})
	assert r.status_code == 401

# Account already exists.
def test_admin_user_post_409():
	r = admin.post(API+"/admin/user", json={
		"uid": 0xdeadbeef,
		"email": None,
		"points": None,
		"claimed": False,
		"custom": None,
		"privilege": 0
	})
	assert r.status_code == 409

# --[ CLAIM AN ACCOUNT ]--

# Success.
def test_user_user_post_201():
	r = requests.post(API+"/user/user", data={
		"uid": 0xdeadbeef,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 201

# Bad form.
def test_user_user_post_400():
	r = requests.post(API+"/user/user", data={
		"uid": 0xdeadbeef,
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 400

# No account with that UID exists.
def test_user_user_post_404():
	r = requests.post(API+"/user/user", data={
		"uid": 9999,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 404

# Account already claimed.
def test_user_user_post_409():
	r = requests.post(API+"/user/user", data={
		"uid": 0xdeadbeef,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 409

# --[ GET INFO ABOUT YOUR OWN ACCOUNT ]--

# Success.
def test_user_user_get_200():
	r = user.get(API+"/user/user")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["id"] == 2
	assert data["uid"] == 0xf00df00d
	assert data["email"] == "user@test.com"
	assert data["points"] == None
	assert data["claimed"] == True

# --[ UPDATE INFO ABOUT YOUR OWN ACCOUNT ]--

# Success.
def test_user_user_patch_200():
	r = user.patch(API+"/user/user", json={
		"uid": 0xf00df00d,
		"email": "test@example.com",
		"password": "********",
		"custom": "",
	})
	assert r.status_code == 200

	r = user.get(API+"/user/user")
	data = json.loads(r.content)
	assert data["email"] == "test@example.com"

# Bad form.
def test_user_user_patch_400():
	r = user.patch(API+"/user/user", json={
		"uid": 0xf00df00d,
		"password": "********",
		"custom": "",
	})
	assert r.status_code == 400

# --[ GET INFO ABOUT ALL ACCOUNTS ]--

# Success.
def test_admin_user_get_200():
	r = admin.get(API+"/admin/user")
	data = json.loads(r.content)
	assert r.status_code == 200 and len(data) > 0

# Bad permissions.
def test_admin_user_get_401():
	r = user.get(API+"/admin/user")
	assert r.status_code == 401

# --[ GET INFO ABOUT A SPECIFIC ACCOUNT ]--

# Success.
def test_admin_user_get_specific_200():
	r = admin.get(API+"/admin/user/1")
	data = json.loads(r.content)
	assert r.status_code == 200
	assert data["email"] == "admin@test.com"

# Bad form.
def test_admin_user_get_specific_400():
	r = admin.get(API+"/admin/user/abc")
	data = json.loads(r.content)
	assert r.status_code == 400

# Bad permissions.
def test_admin_user_get_specific_401():
	r = user.get(API+"/admin/user/1")
	data = json.loads(r.content)
	assert r.status_code == 401

# Account doesn't exist.
def test_admin_user_get_specific_404():
	r = admin.get(API+"/admin/user/999")
	data = json.loads(r.content)
	assert r.status_code == 404

# --[ EDIT INFO ABOUT AN ACCOUNT ]--

# Success.
def test_admin_user_patch_200():
	r = admin.patch(API+"/admin/user/3", json={
		"uid": 0xdeadbeef,
		"email": "jdoe@email.com",
		"points": 100,
		"claimed": True,
		"custom": "",
		"privilege": 0
	})
	assert r.status_code == 200

	s = requests.Session()
	r = s.post(ENDPOINT+"/login", data={"uid": 0xdeadbeef, "password": "hunter2"})
	assert r.status_code == 200
	r = s.get(API+"/user/user")
	data = json.loads(r.content)
	assert data["points"] == 100

# Bad form.
def test_admin_user_patch_400():
	r = admin.patch(API+"/admin/user/3", json={
		"uid": 0xdeadbeef,
		"points": 100,
		"claimed": True,
		"custom": "",
		"privilege": 0
	})
	assert r.status_code == 400

# Bad permissions.
def test_admin_user_patch_401():
	r = user.patch(API+"/admin/user/3", json={
		"uid": 0xdeadbeef,
		"email": "jdoe@email.com",
		"points": 999,
		"claimed": True,
		"custom": "",
		"privilege": 0
	})
	assert r.status_code == 401

# --[ DELETE AN ACCOUNT ]--

# Success.
def test_admin_user_delete_200():
	r = admin.delete(API+"/admin/user/3")
	assert r.status_code == 200

# Bad permissions.
def test_admin_user_delete_401():
	r = user.delete(API+"/admin/user/3")
	assert r.status_code == 401

# User doesn't exist.
def test_admin_user_delete_404():
	r = admin.delete(API+"/admin/user/3")
	assert r.status_code == 404

