import time

from app import *

from flask_login import LoginManager, current_user, login_required, login_user, logout_user

# This is for testing. Delete later.
if User.query.filter_by(uid=0xfeedf00d).first() == None:
	u = User(privilege=User.PRIV_ADMIN, claimed=False, uid=0xfeedf00d)
	u.claim("admin@test.com", "admin", "")
	db.session.add(u)
	db.session.commit()
if User.query.filter_by(uid=0xf00df00d).first() == None:
	u = User(privilege=User.PRIV_USER, claimed=False, uid=0xf00df00d)
	u.claim("user@test.com", "user", "")
	db.session.add(u)
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

def admin_required(f):
	"""
	Decorator that requires the current user be an admin, else return a 401.
	"""

	@login_required
	def wrapper(*args, **kwargs):
		if current_user.privilege != User.PRIV_ADMIN:
			return {}, 401
		return f(*args, **kwargs)

	wrapper.__name__ = f.__name__
	return wrapper

