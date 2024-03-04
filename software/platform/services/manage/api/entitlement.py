from app import *

@app.route(API+"/entitlement", methods=["GET"])
@failsafe_500
# nodoc
def entitlement_get():
	entitlements = [str(e) for e in Entitlement.query.all()]
	return entitlements, 200

@app.route(API+"/entitlement", methods=["POST"])
@failsafe_500
def entitlement_post():

	try:
		# These are required fields for this method.
		for k in ("title", "quantity"):
			assert k in request.json.keys()
		title = request.json["title"]
		quantity = int(request.json["quantity"])
	except:
		return {}, 400

	# Must be unique.
	try:
		assert not Entitlement.query.filter_by(title=title).first()
	except:
		return {}, 409

	db.session.add(Entitlement(title, quantity))
	db.session.commit()

	return {}, 201

@app.route(API+"/entitlement/<entitlementId>", methods=["PATCH"])
@failsafe_500
def entitlement_patch(entitlementId: int):

	try:
		# These are required fields for this method.
		for k in ("title", "quantity"):
			assert k in request.json.keys()
		entitlementId = int(entitlementId)
		title = request.json["title"]
		quantity = int(request.json["quantity"])
	except:
		return {}, 400

	try:
		e = Entitlement.query.get(entitlementId)
		assert e
	except:
		return {}, 404

	# Must be unique.
	try:
		assert not Entitlement.query.filter_by(title=title).first()
	except:
		return {}, 409

	e.title = title
	e.quantity = quantity
	db.session.commit()

	return {}, 200

@app.route(API+"/entitlement/<entitlementId>", methods=["DELETE"])
@failsafe_500
def entitlement_delete(entitlementId: int):

	try:
		entitlementId = int(entitlementId)
	except:
		return {}, 400

	try:
		e = Entitlement.query.get(entitlementId)
		assert e
	except:
		return {}, 404

	db.session.delete(e)
	db.session.commit()

	return {}, 200

