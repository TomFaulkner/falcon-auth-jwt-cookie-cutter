This is a cookie cutter for Falcon with Falcon-Auth using JWT Authentication on Python 3.7 (rc-stretch).

`.env` needs to have a secret key, any string, populated in it. It is included here, but is in the .gitignore file, anyone using this should be sure not to commit the file.

Requirements are pipenv, Docker, Docker-Compose, and an environment that can run make and bash.

License: Do whatever you want with it, if I did something wrong or there is room for improvement please make an issue or a pull request.

To try it out, run

    make build; make run
    curl localhost:5000 token
    curl -H "authorization: jwt yourtokenfromthelaststephere" localhost:5000

The example code with the two API classes isn't ideal, but serves as example for dealing with the JWT.
