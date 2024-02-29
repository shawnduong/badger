import requests

def test_reset_post_0():
	r = requests.post("http://localhost:64094/api/v1/public/reset", json='{"email": "bar@email.com"}')
	assert r.status_code == 202

def test_reset_post_1():
	r = requests.post("http://localhost:64094/api/v1/public/reset", json='{"email": "bar@emailcom"}')
	assert r.status_code == 400

def test_reset_post_2():
	r = requests.post("http://localhost:64094/api/v1/public/reset", json='{"email": "baremail.com"}')
	assert r.status_code == 400

def test_reset_post_3():
	r = requests.post("http://localhost:64094/api/v1/public/reset", json='{"email": "baremailcom"}')
	assert r.status_code == 400

def test_reset_post_4():
	r = requests.post("http://localhost:64094/api/v1/public/reset", json='{"emil": "bar@email.com"}')
	assert r.status_code == 400
