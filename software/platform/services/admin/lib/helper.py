def failsafe_500(f):
	"""
	Decorator that tries to execute f and if it fails, return a generic 500
	error with no additional data.
	"""

	def wrapper(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except Exception as e:
			print("--- CUT HERE FOR EXCEPTION ---")
			print("Ran into an exception.")
			print(e)
			print(args)
			print(kwargs)
			print("--- END EXCEPTION ---")
			return {}, 500

	wrapper.__name__ = f.__name__
	return wrapper

