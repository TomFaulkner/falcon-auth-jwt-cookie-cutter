import os

SECRET = os.environ.get('JWT_SECRET')
assert SECRET is not None, "No JWT Secret key found."
