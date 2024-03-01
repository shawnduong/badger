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
		  "points": 300,
		  "claimed": True,
		  "custom": "e2N1c3RvbUZpZWxkOjEwfQo=",
		  "privilege": 0
		})
	assert r.status_code == 400

def test_admin_user_post_1():
	r = r1.post(api+"/admin/user", json={
		  "uid": 3735928559, # 0xdeadbeef
		  "email": "jdoe@email.com",
		  "points": 300,
		  "claimed": True,
		  "custom": "e2N1c3RvbUZpZWxkOjEwfQo=",
		  "privilege": 0
		})
	assert r.status_code == 201

def test_admin_user_post_2():
	r = r1.post(api+"/admin/user", json={
		  "uid": 3735928559, # 0xdeadbeef
		  "email": "jdoe@email.com",
		  "points": 300,
		  "claimed": True,
		  "custom": "e2N1c3RvbUZpZWxkOjEwfQo=",
		  "privilege": 0
		})
	assert r.status_code == 409

def test_admin_user_post_3():
	r = r2.post(api+"/admin/user", json={
		  "uid": 3735928560,
		  "email": "jdoe123@email.com",
		  "points": 300,
		  "claimed": True,
		  "custom": "e2N1c3RvbUZpZWxkOjEwfQo=",
		  "privilege": 0
		})
	assert r.status_code == 401

