import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

admin = requests.Session()
admin.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

user = requests.Session()
user.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# --[ GET THE POLICY ]--

# Success.
def test_admin_policy_get_200():
	r = admin.get(API+"/admin/policy")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["requireRegistration"] == True
	assert data["selfServiceAccountReset"] == False
	assert data["selfServiceAccountResetExpiry"] == None

# Bad permissions.
def test_admin_policy_get_401():
	r = user.get(API+"/admin/policy")
	assert r.status_code == 401

# --[ CHANGE THE POLICY ]--

# Bad form.
def test_admin_policy_patch_400():
	r = admin.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
	})
	assert r.status_code == 400

# Success.
def test_admin_policy_patch_200():
	r = admin.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
		"selfServiceAccountResetExpiry": None
	})
	assert r.status_code == 200

	r = admin.get(API+"/admin/policy")
	assert r.status_code == 200

	data = json.loads(r.content)
	assert data["requireRegistration"] == False
	assert data["selfServiceAccountReset"] == False
	assert data["selfServiceAccountResetExpiry"] == None

# Bad permissions.
def test_admin_policy_patch_401():
	r = user.patch(API+"/admin/policy", json={
		"requireRegistration": False,
		"selfServiceAccountReset": False,
	})
	assert r.status_code == 401

# --[ MAKE A SCANNER CONFIGURATION ]--

# Success.
def test_admin_configure_post_200():
	r = admin.post(API+"/admin/configure", json={
		"scannerId": 1,
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 201

# Bad form.
def test_admin_configure_post_400_0():
	r = admin.post(API+"/admin/configure", json={
		"scannerId": 2,
		"schedule": {
			"timestamp": 1704067200,
			"display": "Check-In Station",
			"mode": "check-in"
		},
	})
	assert r.status_code == 400

# Bad form.
def test_admin_configure_post_400_1():
	r = admin.post(API+"/admin/configure", json={
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 400

# Bad form.
def test_admin_configure_post_400_2():
	r = admin.post(API+"/admin/configure", json={
		"scannerId": 1,
	})
	assert r.status_code == 400

# Unauthorized.
def test_admin_configure_post_401():
	r = user.post(API+"/admin/configure", json={
		"scannerId": 1,
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 401

# Configuration for this scanner ID already exists.
def test_admin_configure_post_409():
	r = admin.post(API+"/admin/configure", json={
		"scannerId": 1,
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 409

# --[ UPDATE A SCANNER CONFIGURATION ]--

# Success.
def test_admin_configure_patch_200():
	r = admin.patch(API+"/admin/configure/1", json={
		"scannerId": 2,
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 200

# Bad client form.
def test_admin_configure_patch_400():
	r = admin.patch(API+"/admin/configure/1", json={
		"scannerId": 2,
	})
	assert r.status_code == 400

# Unauthorized
def test_admin_configure_patch_401():
	r = user.patch(API+"/admin/configure/1", json={
		"scannerId": 2,
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 401

# Configuration not found.
def test_admin_configure_patch_404():
	r = admin.patch(API+"/admin/configure/9600", json={
		"scannerId": 2,
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 404

# Configuration for this scanner already exists.
def test_admin_configure_patch_409():

	# This is what configuration id 1 will collide with.
	r = admin.post(API+"/admin/configure", json={
		"scannerId": 5,
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 201

	# This existing config will collide with that.
	r = admin.patch(API+"/admin/configure/1", json={
		"scannerId": 5,
		"schedule": [
			{
				"timestamp": 1704067200,
				"display": "Check-In Station",
				"mode": "check-in"
			},
			{
				"timestamp": 1704067200+3600,
				"display": "Event ABC",
				"mode": "attendance"
			},
		]
	})
	assert r.status_code == 409

# --[ GET THE SCANNER CONFIGURATIONS ]--

# Success.
def test_admin_configure_get_200():

	r = admin.get(API+"/admin/configure")
	assert r.status_code == 200

	data = [json.loads(obj) for obj in json.loads(r.content)]
	assert data == [
		{
			"scannerId": 2,
			"schedule": [
				{
					"timestamp": 1704067200,
					"display": "Check-In Station",
					"mode": "check-in"
				},
				{
					"timestamp": 1704067200+3600,
					"display": "Event ABC",
					"mode": "attendance"
				},
			],
			"id": 1
		},
		{
			"scannerId": 5,
			"schedule": [
				{
					"timestamp": 1704067200,
					"display": "Check-In Station",
					"mode": "check-in"
				},
				{
					"timestamp": 1704067200+3600,
					"display": "Event ABC",
					"mode": "attendance"
				},
			],
			"id": 2
		},
	]

# Unauthorized.
def test_admin_configure_get_401():
	r = user.get(API+"/admin/configure")
	assert r.status_code == 401

# --[ DELETE A CONFIGURATION ]--

# Success.
def test_admin_configure_delete_200():
	r = admin.delete(API+"/admin/configure/1")
	assert r.status_code == 200
	r = admin.delete(API+"/admin/configure/2")
	assert r.status_code == 200

# Bad client form.
def test_admin_configure_delete_400():
	r = admin.delete(API+"/admin/configure/foo")
	assert r.status_code == 400

# Unauthorized.
def test_admin_configure_delete_401():
	r = user.delete(API+"/admin/configure/1")
	assert r.status_code == 401

# Configuration not found.
def test_admin_configure_delete_404():
	r = admin.delete(API+"/admin/configure/1")
	assert r.status_code == 404

