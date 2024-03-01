import json
import requests

endpoint = "http://localhost:8080"
api = endpoint+"/api/v1/"

r1 = requests.Session()
r1.post(endpoint+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

r2 = requests.Session()
r2.post(endpoint+"/login", data={"uid": 0xf00df00d, "password": "user"})

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

def test_admin_get_user_0():
	r = r1.get(api+"/admin/user")
	data = json.loads(r.content)
	assert r.status_code == 200 and len(data) > 0

