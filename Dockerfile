FROM python:rc-stretch
WORKDIR /usr/src/app

COPY Pipfile* ./
COPY ./backend/project .
RUN pip install pipenv
RUN pipenv install --deploy

CMD ["pipenv", "run", "gunicorn", "-b 0.0.0.0:5000", "main:app"]
