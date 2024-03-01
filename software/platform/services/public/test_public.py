import requests

API = "http://localhost:64094/api/v1/public"

def test_reset_post_0():
	r = requests.post(API+"/reset", json='{"email": "bar@email.com"}')
	assert r.status_code == 202

def test_reset_post_1():
	r = requests.post(API+"/reset", json='{"email": "bar@emailcom"}')
	assert r.status_code == 400

def test_reset_post_2():
	r = requests.post(API+"/reset", json='{"email": "baremail.com"}')
	assert r.status_code == 400

def test_reset_post_3():
	r = requests.post(API+"/reset", json='{"email": "baremailcom"}')
	assert r.status_code == 400

def test_reset_post_4():
	r = requests.post(API+"/reset", json='{"emil": "bar@email.com"}')
	assert r.status_code == 400
