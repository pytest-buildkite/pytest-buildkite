
MAIN_MODULE := pyruncompare
MODULES := $(MAIN_MODULE) test
ARGS ?= "--python 3.7"

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: _test
_test: ## Run Testing 
	python -m flake8 $(MODULES)
	python -m pylint $(MODULES)
	python -m bandit -r $(MAIN_MODULE)
	python -m pytest --cov-report term --cov-report xml:cov.xml --cov=$(MAIN_MODULE)
	echo 'Testing Complete'

.PHONY: _pipenv
_pipenv: ## Run PIPENV
	python -m pipenv $(ARGS)

.PHONY: _publish
_publish: ## Publish to Pypi
	python setup.py bdist_wheel sdist
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	python -m twine upload dist/*

