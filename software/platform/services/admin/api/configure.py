from app import *

import json

@app.route(API+"/configure", methods=["GET"])
@failsafe_500
def configure_get():
	configurations = [str(c) for c in Configuration.query.all()]
	return configurations, 200

@app.route(API+"/configure/lookup/<scannerId>", methods=["GET"])
@failsafe_500
# nodoc
def configure_get_lookup():

	configuration = Configuration.query.filter_by(scannerId=int(scannerId))

	if not configuration:
		return {}, 404

	return str(configuration), 200

@app.route(API+"/configure", methods=["POST"])
@failsafe_500
def configure_post():

	try:
		# These are required fields for this method.
		for k in ("authorization", "scannerId", "schedule"):
			assert k in request.json.keys()
		scannerId = int(request.json["scannerId"])
		assert type(request.json["schedule"]) is list
		json.dumps(request.json["schedule"])
	except:
		return {}, 400

	# There must not be another configuration already with this scanner ID.
	try:
		assert not Configuration.query.filter_by(scannerId=scannerId).first()
	except:
		return {}, 409

	db.session.add(Configuration(request.json["authorization"], scannerId, request.json["schedule"]))
	db.session.commit()

	return {}, 201

@app.route(API+"/configure/<configurationId>", methods=["PATCH"])
@failsafe_500
def configure_patch(configurationId: int):

	try:
		# These are required fields for this method.
		for k in ("authorization", "scannerId", "schedule"):
			assert k in request.json.keys()
		configurationId = int(configurationId)
		scannerId = int(request.json["scannerId"])
		assert type(request.json["schedule"]) is list
#		schedule = json.dumps(request.json["schedule"])
		json.dumps(request.json["schedule"])
	except:
		return {}, 400

	# The configuration must exist.
	try:
		assert (c:=Configuration.query.get(configurationId))
	except:
		return {}, 404

	# There must not be another configuration already with this scanner ID.
	try:
		assert not Configuration.query.filter_by(scannerId=scannerId).first()
	except:
		return {}, 409

	c.authorization = request.json["authorization"]
	c.scannerId = scannerId
	c.schedule = json.dumps(request.json["schedule"])
	db.session.commit()

	return {}, 200

@app.route(API+"/configure/<configurationId>", methods=["DELETE"])
@failsafe_500
def configure_delete(configurationId: int):

	try:
		configurationId = int(configurationId)
	except:
		return {}, 400

	try:
		assert (c:=Configuration.query.get(configurationId))
	except:
		return {}, 404

	db.session.delete(c)
	db.session.commit()

	return {}, 200

