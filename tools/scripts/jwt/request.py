import sys

try:
    import requests
except ImportError:
    print("Requests, a dev requirement, must be installed to use this.")
    sys.exit(1)


def fetch_token():
    resp = requests.get('http://localhost:5000/token')
    if resp.ok:
        return resp.text
    return (f"Something went wrong, response data: {resp.status_code}"
            f"\n{resp.text}")


if __name__ == '__main__':
    print(fetch_token())
