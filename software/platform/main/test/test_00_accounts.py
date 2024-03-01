import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

r1 = requests.Session()
r1.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

r2 = requests.Session()
r2.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ MAKE AN ACCOUNT ]--

def test_admin_user_post_0():
	r = r1.post(API+"/admin/user", json={
		"uid": 0xdeadbeef,
		"points": None,
		"claimed": False,
		"custom": None,
		"privilege": 0
	})
	assert r.status_code == 400

def test_admin_user_post_1():
	r = r1.post(API+"/admin/user", json={
		"uid": 0xdeadbeef,
		"email": None,
		"points": None,
		"claimed": False,
		"custom": None,
		"privilege": 0
	})
	assert r.status_code == 201

def test_admin_user_post_2():
	r = r1.post(API+"/admin/user", json={
		"uid": 0xdeadbeef,
		"email": None,
		"points": None,
		"claimed": False,
		"custom": None,
		"privilege": 0
	})
	assert r.status_code == 409

def test_admin_user_post_3():
	r = r2.post(API+"/admin/user", json={
		"uid": 0xdeadbeef+1,
		"email": None,
		"points": None,
		"claimed": False,
		"custom": None,
		"privilege": 0
	})
	assert r.status_code == 401

# --[ CLAIM AN ACCOUNT ]--

def test_user_user_post_0():
	r = requests.post(API+"/user/user", data={
		"uid": 0xdeadbeef,
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 400

def test_user_user_post_1():
	r = requests.post(API+"/user/user", data={
		"uid": 0xdeadbeef,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 201

def test_user_user_post_2():
	r = requests.post(API+"/user/user", data={
		"uid": 0xdeadbeef,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 409

def test_user_user_post_3():
	r = requests.post(API+"/user/user", data={
		"uid": 9999,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 400

# --[ GET INFO ABOUT YOUR OWN ACCOUNT ]--

def test_user_user_get_0():
	r = r2.get(API+"/user/user")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["id"] == 2
	assert data["uid"] == 0xf00df00d
	assert data["email"] == "user@test.com"
	assert data["points"] == None
	assert data["claimed"] == True

# --[ UPDATE INFO ABOUT YOUR OWN ACCOUNT ]--

def test_user_user_patch_0():
	r = r2.patch(API+"/user/user", json={
		"uid": 0xf00df00d,
		"email": "test@example.com",
		"password": "********",
		"custom": "",
	})
	assert r.status_code == 201

	r = r2.get(API+"/user/user")
	data = json.loads(r.content)
	assert data["email"] == "test@example.com"

# --[ GET INFO ABOUT ALL ACCOUNTS ]--

def test_admin_get_user_0():
	r = r1.get(API+"/admin/user")
	data = json.loads(r.content)
	assert r.status_code == 200 and len(data) > 0

def test_admin_get_user_1():
	r = r2.get(API+"/admin/user")
	assert r.status_code == 401

# --[ EDIT INFO ABOUT AN ACCOUNT ]--

def test_admin_patch_user_0():
	r = r1.patch(API+"/admin/user/3", json={
		"uid": 0xdeadbeef,
		"points": 100,
		"claimed": True,
		"custom": "",
		"privilege": 0
	})
	assert r.status_code == 400

	s = requests.Session()
	r = s.post(ENDPOINT+"/login", data={"uid": 0xdeadbeef, "password": "hunter2"})
	assert r.status_code == 200
	r = s.get(API+"/user/user")
	data = json.loads(r.content)
	assert data["points"] == None

def test_admin_patch_user_1():
	r = r1.patch(API+"/admin/user/3", json={
		"uid": 0xdeadbeef,
		"email": "jdoe@email.com",
		"points": 100,
		"claimed": True,
		"custom": "",
		"privilege": 0
	})
	assert r.status_code == 201

	s = requests.Session()
	r = s.post(ENDPOINT+"/login", data={"uid": 0xdeadbeef, "password": "hunter2"})
	assert r.status_code == 200
	r = s.get(API+"/user/user")
	data = json.loads(r.content)
	assert data["points"] == 100

def test_admin_patch_user_2():
	r = r2.patch(API+"/admin/user/3", json={
		"uid": 0xdeadbeef,
		"email": "jdoe@email.com",
		"points": 999,
		"claimed": True,
		"custom": "",
		"privilege": 0
	})
	assert r.status_code == 401

# --[ DELETE AN ACCOUNT ]--

def test_admin_user_delete_0():
	r = r1.delete(API+"/admin/user/3")
	assert r.status_code == 200

def test_admin_user_delete_1():
	r = r1.delete(API+"/admin/user/3")
	assert r.status_code == 404

def test_admin_user_delete_2():
	r = r2.delete(API+"/admin/user/3")
	assert r.status_code == 401

