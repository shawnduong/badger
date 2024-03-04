from app import *

@app.route(API+"/claim", methods=["GET"])
@failsafe_500
def claim_get():
	claims = [str(claim) for claim in Claim.query.all()]
	return claims, 200

@app.route(API+"/claim", methods=["POST"])
@failsafe_500
def claim_post():

	try:
		# These are required fields for this method.
		for k in ("rewardId", "userId", "retrieved"):
			assert k in request.json.keys()
		rewardId = int(request.json["rewardId"])
		userId = int(request.json["userId"])
		retrieved = bool(request.json["retrieved"])
	except:
		return {}, 400

	# It is the responsibility of the caller to make sure that the user exists
	# and return a 404 if not.
	try:
		assert Reward.query.get(rewardId)
	except:
		return {}, 404

	claim = Claim(rewardId, userId, retrieved)
	db.session.add(claim)
	db.session.commit()

	return {}, 201

@app.route(API+"/claim/<claimId>", methods=["PATCH"])
@failsafe_500
def claim_patch(claimId: int):

	try:
		# These are required fields for this method.
		for k in ("rewardId", "userId", "retrieved"):
			assert k in request.json.keys()
		claimId = int(claimId)
		rewardId = int(request.json["rewardId"])
		userId = int(request.json["userId"])
		retrieved = bool(request.json["retrieved"])
	except:
		return {}, 400

	# It is the responsibility of the caller to make sure that the user exists
	# and return a 404 if not.
	try:
		assert Reward.query.get(rewardId)
		assert (c:=Claim.query.get(claimId))
	except:
		return {}, 404

	c.rewardId = rewardId
	c.userId = userId
	c.retrieved = retrieved
	db.session.commit()

	return {}, 200

@app.route(API+"/claim/<claimId>", methods=["DELETE"])
@failsafe_500
def claim_delete(claimId: int):

	try:
		claimId = int(claimId)
	except:
		return {}, 400

	try:
		assert (c:=Claim.query.get(claimId))
	except:
		return {}, 404

	db.session.delete(c)
	db.session.commit()

	return {}, 200

