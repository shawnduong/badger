import requests

from app import *

from flask_login import current_user, login_required

adminPrefix = "/api/v1/admin"

@app.route(adminPrefix+"/user", methods=["POST"])
@admin_required
def admin_user_post():
	"""
	Create a user account. This is different than User's POST user method,
	which fills out the information in the account made here.
	"""

	return {}, 200
