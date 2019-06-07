
ARGS ?= "--python 3.7"

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: _build
_build: ## Prepare Docker Image
	python -m pip install pipenv

.PHONY: _pipenv
_pipenv: ## Prepare Docker Image
	pwd
	python -m pipenv $(ARGS)

