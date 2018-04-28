import falcon
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend

from routes import routes
from constants import SECRET


def user_loader(user):
    return {'username': user}


auth_backend = JWTAuthBackend(user_loader,
                              SECRET,
                              algorithm="HS256",
                              leeway=30)
auth_middleware = FalconAuthMiddleware(
    auth_backend,
    exempt_routes=['/token'],
    exempt_methods=['HEAD', 'OPTIONS'])
app = falcon.API(middleware=[auth_middleware])

for endpoint, object in routes:
    app.add_route(endpoint, object)
