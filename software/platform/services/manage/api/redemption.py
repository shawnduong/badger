from app import *

@app.route(API+"/redemption", methods=["GET"])
@failsafe_500
def redemption_get():
	redemptions = [str(r) for r in Redemption.query.all()]
	return redemptions, 200

@app.route(API+"/redemption/lookup/<userId>", methods=["GET"])
@failsafe_500
def redemption_get_lookup(userId: int):
	redemptions = [str(r) for r in Redemption.query.filter_by(userId=userId)]
	return redemptions, 200

@app.route(API+"/redemption", methods=["POST"])
@failsafe_500
def redemption_post():

	try:
		# These are required fields for this method.
		for k in ("entitlementId", "userId"):
			assert k in request.json.keys()
		entitlementId = int(request.json["entitlementId"])
		userId = int(request.json["userId"])
	except:
		return {}, 400

	# It is the responsibility of the caller to make sure that the user exists
	# and return a 404 if not.
	try:
		assert (entitlement:=Entitlement.query.get(entitlementId))
	except:
		return {}, 404

	# This redemption must not go over the maximum allowed.
	try:
		redemptions = Redemption.query.filter_by(
			entitlementId=entitlementId, userId=userId
		).all()
		assert len(redemptions) < entitlement.quantity
	except:
		return {}, 409

	db.session.add(Redemption(entitlementId, userId))
	db.session.commit()

	return {}, 201

@app.route(API+"/redemption/<redemptionId>", methods=["PATCH"])
@failsafe_500
def redemption_patch(redemptionId: int):

	try:
		# These are required fields for this method.
		for k in ("entitlementId", "userId"):
			assert k in request.json.keys()
		redemptionId = int(redemptionId)
		entitlementId = int(request.json["entitlementId"])
		userId = int(request.json["userId"])
	except:
		return {}, 400

	# It is the responsibility of the caller to make sure that the user exists
	# and return a 404 if not.
	try:
		assert (e:=Entitlement.query.get(entitlementId))
		assert (r:=Redemption.query.get(redemptionId))
	except:
		return {}, 404

	# This redemption must not go over the maximum allowed.
	try:
		redemptions = Redemption.query.filter_by(
			entitlementId=entitlementId, userId=userId
		).all()
		assert len(redemptions) < e.quantity
	except:
		return {}, 409

	r.entitlementId = entitlementId
	r.userId = userId
	db.session.commit()

	return {}, 200

@app.route(API+"/redemption/<redemptionId>", methods=["DELETE"])
@failsafe_500
def redemption_delete(redemptionId: int):

	try:
		redemptionId = int(redemptionId)
	except:
		return {}, 400

	try:
		r = Redemption.query.get(redemptionId)
		assert r
	except:
		return {}, 404

	db.session.delete(r)
	db.session.commit()

	return {}, 200

