import time

from app import *

from flask_login import LoginManager, login_required, login_user, logout_user

## If there is no admin account, make a default one.
#if User.query.filter_by(privilege=1).first() == None:
#	u = User(1, False)
#	db.session.add(u)
#	db.session.commit()

# This is for testing. Delete later.
if User.query.filter_by(uid=0xdeadbeef).first() == None:
	u1 = User(0, False, 0xdeadbeef)
	u1.claim("foo1@bar.com", "password1", "")
	db.session.add(u1)
if User.query.filter_by(uid=0xcafebabe).first() == None:
	u2 = User(0, False, 0xcafebabe)
	db.session.add(u2)
if User.query.filter_by(uid=0xbeefcafe).first() == None:
	u3 = User(0, False, 0xbeefcafe)
	db.session.add(u3)
db.session.commit()

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "login"

@loginManager.user_loader
def load_user(id: int):
	return User.query.get(id)

@app.route("/login", methods=["POST"])
def login():

	assert "uid" in request.form.keys() and "password" in request.form.keys()
	user = User.login(request.form["uid"], request.form["password"])

	if user == None:
		time.sleep(1)  # Prevent brute.
		return render_template("index.html", failed=True)

	login_user(user)
	return redirect(url_for("application"))

@app.route("/logout", methods=["GET"])
@login_required
def logout():

	logout_user()
	return redirect(url_for("index"))

