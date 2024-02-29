from app import *

from flask_login import current_user, login_required

class FrontEndRouter:

	@app.route("/", methods=["GET"])
	@app.route("/login", methods=["GET"])
	def index():

		if current_user.is_authenticated:
			return redirect(url_for("application"))
		return render_template("index.html")

	@app.route("/unlock", methods=["POST"])
	def unlock():

		if current_user.is_authenticated:
			return redirect(url_for("application"))

		if "uid" not in request.form.keys():
			return redirect(url_for("index"))

		# TODO: graceful redirect to index with fail.
		try:
			uid = int(request.form["uid"])
		except:
			return {}, 400

		# If the account exists but is not claimed, then the user should
		# register their account.
		if (u:=User.query.filter_by(uid=uid).first()) != None and not u.claimed:
			return redirect(url_for("register", uid=uid))

		return render_template("unlock.html", uid=uid)

	@app.route("/register", methods=["GET"])
	def register():

		if current_user.is_authenticated:
			return redirect(url_for("application"))

		# TODO: graceful redirect to index with fail.
		try:
			uid = int(request.args.get("uid"))
			assert uid
		except:
			return redirect(url_for("index"))

		return render_template("register.html", uid=uid)

	@app.route("/app", methods=["GET"])
	@login_required
	def application():

		return render_template("app.html")

