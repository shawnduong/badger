from app import *

@app.route(API+"/reward", methods=["GET"])
@failsafe_500
# nodoc
def reward_get():
	rewards = [str(r) for r in Reward.query.all()]
	return rewards, 200

@app.route(API+"/reward", methods=["POST"])
@failsafe_500
def reward_post():

	try:
		# These are required fields for this method.
		for k in ("item", "points", "stockTotal"):
			assert k in request.json.keys()
		points = int(request.json["points"])
		stockTotal = int(request.json["stockTotal"])
	except:
		return {}, 400

	# This reward must be unique.
	try:
		print(Reward.query.filter_by(item=request.json["item"]).all())
		assert len(Reward.query.filter_by(item=request.json["item"]).all()) == 0
	except:
		return {}, 409

	db.session.add(Reward(request.json["item"], points, stockTotal))
	db.session.commit()

	return {}, 201

@app.route(API+"/reward/<rewardId>", methods=["PATCH"])
@failsafe_500
def reward_patch(rewardId: int):

	try:
		# These are required fields for this method.
		for k in ("item", "points", "stockTotal"):
			assert k in request.json.keys()
		rewardId = int(rewardId)
		points = int(request.json["points"])
		stockTotal = int(request.json["stockTotal"])
	except:
		return {}, 400

	try:
		assert (r:=Reward.query.get(rewardId))
	except:
		return {}, 404

	# This reward must be unique.
	try:
		if not r.item == request.json["item"]:
			assert len(Reward.query.filter_by(item=request.json["item"]).all()) == 0
	except:
		return {}, 409

	r.item = request.json["item"]
	r.points = points
	r.stockTotal = stockTotal
	db.session.commit()

	return {}, 200

@app.route(API+"/reward/<rewardId>", methods=["DELETE"])
@failsafe_500
def reward_delete(rewardId: int):

	try:
		rewardId = int(rewardId)
	except:
		return {}, 400

	try:
		r = Reward.query.get(rewardId)
		assert r
	except:
		return {}, 404

	db.session.delete(r)
	db.session.commit()

	return {}, 200

