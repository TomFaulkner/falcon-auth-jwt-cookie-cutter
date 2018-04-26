from decode import decode
from request import fetch_token

token = fetch_token()
print(decode(token))
