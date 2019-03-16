.PHONY: help clean coverage dev integrate lint package package-install pypi-install test upload uninstall

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

integrate:
	pytest integrate

lint:
	isort -y
	black .

package:
	python setup.py sdist
	python setup.py bdist_wheel

package-install:
	pip install dist/*.whl

pypi-install:
	pip install -U --no-cache-dir "flake8-fixme==${FLAKE8_FIXME_VERSION}"

test:
	isort --diff
	black --check --diff .
	flake8
	mypy flake8_fixme integrate
	pytest --cov=./ flake8_fixme

upload:
	twine upload dist/*

uninstall:
	pip uninstall -y flake8-fixme
