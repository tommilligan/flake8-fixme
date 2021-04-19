.PHONY: help clean coverage dev integrate lint lint-fix package package-install pypi-install test update upload uninstall

help:
	@echo "This project assumes that an active Python virtualenv is present."


clean:
	rm -rf dist/*

coverage:
	codecov

dev:
	pip install -U pip
	pip install "pipenv==2020.11.15"
	pipenv install --dev --deploy
	pip install -e .

integrate:
	pytest integrate

lint:
	isort --diff .
	black --check --diff .
	flake8
	mypy flake8_fixme
	mypy integrate

lint-fix:
	isort -y .
	black .

package:
	python setup.py sdist
	python setup.py bdist_wheel

package-install:
	pip install dist/*.whl

pypi-install:
	pip install -U --no-cache-dir "flake8-fixme==${FLAKE8_FIXME_VERSION}"

test:
	pytest --cov=./ flake8_fixme

update:
	pipenv lock
	pipenv install --dev --deploy

upload:
	twine upload dist/*

uninstall:
	pip uninstall -y flake8-fixme
