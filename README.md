This is a cookie cutter for Falcon with Falcon-Auth using JWT Authentication on Python 3.7 (rc-stretch) in a Docker container.

`.env` needs to have a secret key, which can be any string. It is included here, but is in the .gitignore file, anyone using this should __be sure not to commit the file.__

##Requirements

pipenv, Docker 2+, Docker-Compose

###Nice to have

Not absolutely required, but for ease of use: and an environment that can run `make` and `bash`.

##Usage

To try it out, run

    make build; make run
    curl localhost:5000 token
    curl -H "authorization: jwt yourtokenfromthelaststephere" localhost:5000
    
There are three Python scripts in `tools/scripts/jwt` to request a token, decode a token, and one that does both. To use the decoder, pipe the token to `decode.py`. (`echo $TOKEN | python3 decode.py`)

##License

Do whatever you want with it.

##Contributing

If I did something wrong or there is room for improvement please make an issue or a pull request.

