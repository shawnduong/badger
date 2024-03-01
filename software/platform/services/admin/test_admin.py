import json
import requests

API = "http://localhost:64097/api/v1/admin"

def test_policy_get_0():
	r = requests.get(API+"/policy")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["requireRegistration"] == True
	assert data["selfServiceAccountReset"] == False
	assert data["selfServiceAccountResetExpiry"] == None

def test_policy_patch_0():
	r = requests.patch(API+"/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
	})
	assert r.status_code == 400

def test_policy_patch_1():
	r = requests.patch(API+"/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
		"selfServiceAccountResetExpiry": None
	})
	assert r.status_code == 200

	r = requests.get(API+"/policy")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["requireRegistration"] == False
	assert data["selfServiceAccountReset"] == False
	assert data["selfServiceAccountResetExpiry"] == None

