import os
from datetime import datetime, timedelta

import jwt

SECRET = os.environ.get('JWT_SECRET')
assert SECRET is not None, "No JWT Secret key found."


def issue(claims: dict,
          expire: datetime = datetime.utcnow() + timedelta(days=5)) -> str:
    """Create JWT Token
    """
    claims['exp'] = expire
    claims['iat'] = datetime.utcnow()
    claims['nbf'] = claims['iat'] - timedelta(seconds=60)
    token = jwt.encode(claims, SECRET, algorithm='HS256')
    return token
