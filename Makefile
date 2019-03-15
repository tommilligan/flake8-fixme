.PHONY: help clean coverage dev lint package test upload

help:
	@echo "This project assumes that an active Python virtualenv is present."

clean:
	rm -rf dist/*

coverage:
	codecov

dev:
	pip install "pipenv==2018.11.26"
	pipenv install --dev --deploy
	pip install -e .

lint:
	isort -y
	black .

package:
	python setup.py sdist
	python setup.py bdist_wheel

test:
	isort --diff
	black --check --diff .
	flake8
	mypy flake8_fixme
	pytest --cov=./

upload:
	twine upload dist/*
