from datetime import datetime, timedelta

import jwt

from constants import SECRET


def _issue(claims: dict,
           expire: datetime = datetime.utcnow() + timedelta(days=5)) -> str:
    """Create JWT Token
    """
    claims['exp'] = expire
    claims['iat'] = datetime.utcnow()
    claims['nbf'] = claims['iat'] - timedelta(seconds=60)
    token = jwt.encode(claims, SECRET, algorithm='HS256')
    return token


class JWTIssuer:
    """Issues JWTs, on its own it does not authentication, just issues.
    """

    def on_get(self, req, resp):
        resp.body = _issue({'hello': 'world'})


class JWTDecoder:
    """Returns values stored in JWT.
    """

    def on_get(self, req, resp):
        user = req.context['user']
        resp.body = "User Found: {}".format(user['username'])
