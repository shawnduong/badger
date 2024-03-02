import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

admin = requests.Session()
admin.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

user = requests.Session()
user.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ MAKE A CODE ]--

# Bad form.
def test_manage_code_post_400():
	r = admin.post(API+"/manage/code", json={
		"code": "AAAA-BB-CCCC",
	})
	assert r.status_code == 400

# Success.
def test_manage_code_post_201():
	r = admin.post(API+"/manage/code", json={
		"code": "AAAA-BB-CCCC",
		"points": 100
	})
	assert r.status_code == 201

# Code already exists.
def test_manage_code_post_409():
	r = admin.post(API+"/manage/code", json={
		"code": "AAAA-BB-CCCC",
		"points": 100
	})
	assert r.status_code == 409

# Bad permissions.
def test_manage_code_post_401():
	r = user.post(API+"/manage/code", json={
		"code": "2222-11-0000",
		"points": 50
	})
	assert r.status_code == 401

# --[ GET CODES ]--

# Success.
def test_manage_code_get_200():

	r = admin.get(API+"/manage/code")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["code"] == "AAAA-BB-CCCC"
	assert data[0]["points"] == 100
	assert data[0]["id"] == 1

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

# Bad form.
def test_manage_code_patch_400():
	r = admin.patch(API+"/manage/code/1", json={
		"code": "AAAA-BB-CCCC",
	})
	assert r.status_code == 400

# Code doesn't exist.
def test_manage_code_patch_404():
	r = admin.patch(API+"/manage/code/9999", json={
		"code": "AAAA-BB-CCCC",
		"points": 250
	})
	assert r.status_code == 404

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

# Bad permissions.
def test_manage_code_patch_401():

	r = user.patch(API+"/manage/code/1", json={
		"code": "AAAA-BB-CCCC",
		"points": 999
	})
	assert r.status_code == 401

# --[ DELETE A CODE ]--

# Code doesn't exist.
def test_manage_code_delete_404():
	r = admin.delete(API+"/manage/code/999")
	assert r.status_code == 404

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
