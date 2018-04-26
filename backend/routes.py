from api.user.auth import JWTIssuer, JWTDecoder

routes = [
    ('/decoder', JWTDecoder()),
    ('/token', JWTIssuer())
]
