from app import *

import json
import re

@app.route(API+"/code", methods=["GET"])
@failsafe_500
def code_get():

	codes = [str(code) for code in Code.query.all()]
	return codes, 200

@app.route(API+"/code", methods=["POST"])
@failsafe_500
def code_post():

	try:
		# These are required fields for this method.
		for k in ("code", "points"):
			assert k in request.json.keys()
		int(request.json["points"])
	except:
		return {}, 400

	try:
		assert Code.query.filter_by(code=request.json["code"]).first() == None
	except:
		return {}, 409

	code = Code(request.json["code"], request.json["points"])
	db.session.add(code)
	db.session.commit()

	return {}, 201

@app.route(API+"/code/<codeId>", methods=["GET"])
@failsafe_500
def code_get_specific(codeId: int):

	try:
		int(codeId)
	except:
		return {}, 400

	try:
		assert (c:=Code.query.get(codeId))
	except:
		return {}, 404

	return str(c), 200

@app.route(API+"/code/<codeId>", methods=["PATCH"])
@failsafe_500
def code_patch(codeId):

	try:
		# These are required fields for this method.
		for k in ("code", "points"):
			assert k in request.json.keys()
		int(request.json["points"])
	except:
		return {}, 400

	try:
		assert (c:=Code.query.get(codeId))
	except:
		return {}, 404

	c.code = request.json["code"]
	c.points = request.json["points"]
	db.session.commit()

	return {}, 200

@app.route(API+"/code/<codeId>", methods=["DELETE"])
@failsafe_500
def code_delete(codeId):

	try:
		assert (c:=Code.query.get(codeId))
	except:
		return {}, 404

	db.session.delete(c)
	db.session.commit()

	return {}, 200

