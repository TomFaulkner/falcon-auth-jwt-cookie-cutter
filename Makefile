TEST_PATH=./
SHELL := /bin/bash

.PHONY: clean-pyc
clean-pyc:
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm --force {} +

.PHONY: build
build:
	@sudo docker-compose build

.PHONY: run
run:
	@sudo docker-compose up

.PHONY: lint
lint:
	@flake8 --exclude=.tox

.PHONY: test
test: clean-pyc
	@py.test --verbose --color=yes $(TEST_PATH)
