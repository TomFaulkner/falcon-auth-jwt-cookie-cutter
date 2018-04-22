import os

import falcon
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend

from auth import web_token

SECRET = os.environ.get('JWT_SECRET')
assert SECRET is not None, "No JWT Secret key found."


def user_loader(user):
    return {'username': user}


auth_backend = JWTAuthBackend(user_loader,
                              SECRET,
                              algorithm="HS256",
                              leeway=30)
auth_middleware = FalconAuthMiddleware(auth_backend, exempt_routes=['/token'],
                                       exempt_methods=['HEAD', 'OPTIONS'])
app = falcon.API(middleware=[auth_middleware])


class ApiResource:
    def on_get(self, req, resp):
        user = req.context['user']
        resp.body = "User Found: {}".format(user['username'])


class JWTIssuer:
    def on_get(self, req, resp):
        resp.body = web_token.issue({'hello': 'world'})


app.add_route('/', ApiResource())
app.add_route('/token', JWTIssuer())
