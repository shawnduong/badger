import json
import requests

endpoint = "http://localhost:8080"
api = endpoint+"/api/v1"

r1 = requests.Session()
r1.post(endpoint+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

r2 = requests.Session()
r2.post(endpoint+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ MAKE AN ACCOUNT ]--

def test_admin_user_post_0():
	r = r1.post(api+"/admin/user", json={
		  "uid": 3735928559, # 0xdeadbeef
		  "points": None,
		  "claimed": False,
		  "custom": None,
		  "privilege": 0
		})
	assert r.status_code == 400

def test_admin_user_post_1():
	r = r1.post(api+"/admin/user", json={
		  "uid": 3735928559, # 0xdeadbeef
		  "email": None,
		  "points": None,
		  "claimed": False,
		  "custom": None,
		  "privilege": 0
		})
	assert r.status_code == 201

def test_admin_user_post_2():
	r = r1.post(api+"/admin/user", json={
		  "uid": 3735928559, # 0xdeadbeef
		  "email": None,
		  "points": None,
		  "claimed": False,
		  "custom": None,
		  "privilege": 0
		})
	assert r.status_code == 409

def test_admin_user_post_3():
	r = r2.post(api+"/admin/user", json={
		  "uid": 3735928560,
		  "email": None,
		  "points": None,
		  "claimed": False,
		  "custom": None,
		  "privilege": 0
		})
	assert r.status_code == 401

# --[ CLAIM AN ACCOUNT ]--

def test_user_user_post_0():
	r = requests.post(api+"/user/user", data={
		"uid": 3735928559,
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 400

def test_user_user_post_1():
	r = requests.post(api+"/user/user", data={
		"uid": 3735928559,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 201

def test_user_user_post_2():
	r = requests.post(api+"/user/user", data={
		"uid": 3735928559,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 409

def test_user_user_post_3():
	r = requests.post(api+"/user/user", data={
		"uid": 9999,
		"email": "jdoe@email.com",
		"password": "hunter2",
		"custom": "",
	})
	assert r.status_code == 400

# --[ GET INFO ABOUT YOUR OWN ACCOUNT ]--

def test_user_user_get_0():
	r = r2.get(api+"/user/user")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["id"] == 2
	assert data["uid"] == 0xf00df00d
	assert data["email"] == "user@test.com"
	assert data["points"] == None
	assert data["claimed"] == True

# --[ GET INFO ABOUT ALL ACCOUNTS ]--

def test_admin_get_user_0():
	r = r1.get(api+"/admin/user")
	data = json.loads(r.content)
	assert r.status_code == 200 and len(data) > 0

def test_admin_get_user_1():
	r = r2.get(api+"/admin/user")
	assert r.status_code == 401

# --[ DELETE AN ACCOUNT ]--

def test_admin_user_delete_0():
	r = r1.delete(api+"/admin/user/3")
	assert r.status_code == 200

def test_admin_user_delete_1():
	r = r1.delete(api+"/admin/user/3")
	assert r.status_code == 404

def test_admin_user_delete_2():
	r = r2.delete(api+"/admin/user/3")
	assert r.status_code == 401

