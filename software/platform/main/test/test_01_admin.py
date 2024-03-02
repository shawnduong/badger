import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

admin = requests.Session()
admin.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

user = requests.Session()
user.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ GET THE POLICY ]--

# Success.
def test_admin_policy_get_200():
	r = admin.get(API+"/admin/policy")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["requireRegistration"] == True
	assert data["selfServiceAccountReset"] == False
	assert data["selfServiceAccountResetExpiry"] == None

# Bad permissions.
def test_admin_policy_get_401():
	r = user.get(API+"/admin/policy")
	assert r.status_code == 401

# --[ CHANGE THE POLICY ]--

# Bad form.
def test_admin_policy_patch_400():
	r = admin.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
	})
	assert r.status_code == 400

# Success,
def test_admin_policy_patch_200():
	r = admin.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
		"selfServiceAccountResetExpiry": None
	})
	assert r.status_code == 200

	r = admin.get(API+"/admin/policy")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["requireRegistration"] == False
	assert data["selfServiceAccountReset"] == False
	assert data["selfServiceAccountResetExpiry"] == None

# Bad permissions.
def test_admin_policy_patch_401():
	r = user.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
	})
	assert r.status_code == 401

