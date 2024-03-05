import json
import requests

ENDPOINT = "http://localhost:8080"
API = ENDPOINT+"/api/v1"

admin = requests.Session()
admin.post(ENDPOINT+"/login", data={"uid": 0xfeedf00d, "password": "admin"})

user = requests.Session()
user.post(ENDPOINT+"/login", data={"uid": 0xf00df00d, "password": "user"})

# TODO
