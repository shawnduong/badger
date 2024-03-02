import json
import requests

API = "http://localhost:64096/api/v1/manage"

def test_code_post_0():
	r = requests.post(API+"/code", json={
		"code": "AAAA-BB-CCCC",
	})
	assert r.status_code == 400

def test_code_post_1():
	r = requests.post(API+"/code", json={
		"code": "AAAA-BB-CCCC",
		"points": 100
	})
	assert r.status_code == 201

def test_code_post_2():
	r = requests.post(API+"/code", json={
		"code": "AAAA-BB-CCCC",
		"points": 100
	})
	assert r.status_code == 409

def test_code_post_3():
	r = requests.post(API+"/code", json={
		"code": "2222-11-0000",
		"points": 50
	})
	assert r.status_code == 201

def test_code_get_0():

	r = requests.get(API+"/code")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["code"] == "AAAA-BB-CCCC"
	assert data[0]["points"] == 100
	assert data[0]["id"] == 1
	assert data[1]["code"] == "2222-11-0000"
	assert data[1]["points"] == 50
	assert data[1]["id"] == 2

def test_code_patch_0():
	r = requests.patch(API+"/code/1", json={
		"code": "AAAA-BB-CCCC",
	})
	assert r.status_code == 400

def test_code_patch_1():
	r = requests.patch(API+"/code/9999", json={
		"code": "AAAA-BB-CCCC",
		"points": 250
	})
	assert r.status_code == 404

def test_code_patch_2():

	r = requests.patch(API+"/code/1", json={
		"code": "AAAA-BB-CCCC",
		"points": 250
	})
	assert r.status_code == 200

	r = requests.get(API+"/code")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data[0]["code"] == "AAAA-BB-CCCC"
	assert data[0]["points"] == 250
	assert data[0]["id"] == 1

def test_code_delete_0():
	r = requests.delete(API+"/code/999")
	assert r.status_code == 404

def test_code_delete_1():
	r = requests.delete(API+"/code/1")
	assert r.status_code == 200

	r = requests.delete(API+"/code/1")
	assert r.status_code == 404
