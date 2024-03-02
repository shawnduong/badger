import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

r1 = requests.Session()
r1.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

r2 = requests.Session()
r2.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

def test_admin_policy_get_0():
	r = r1.get(API+"/admin/policy")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["requireRegistration"] == True
	assert data["selfServiceAccountReset"] == False
	assert data["selfServiceAccountResetExpiry"] == None

def test_admin_policy_get_a0():
	r = r2.get(API+"/admin/policy")
	assert r.status_code == 401

def test_admin_policy_patch_0():
	r = r1.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
	})
	assert r.status_code == 400

def test_admin_policy_patch_1():
	r = r1.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
		"selfServiceAccountResetExpiry": None
	})
	assert r.status_code == 200

	r = r1.get(API+"/admin/policy")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["requireRegistration"] == False
	assert data["selfServiceAccountReset"] == False
	assert data["selfServiceAccountResetExpiry"] == None

def test_admin_policy_patch_a0():
	r = r2.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
	})
	assert r.status_code == 401

