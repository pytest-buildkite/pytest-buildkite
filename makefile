
USER := $(shell id -u):$(shell id -g)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: build
build: ## Build the Docker Images
	docker-compose build
	docker-compose up -d
	docker-compose down

.PHONY: initpipenv
initpipenv: ## Prepare pipenv environment 
	docker-compose build
	docker-compose up -d
	docker-compose run -u "$(USER)" app make _initpipenv
	docker-compose down
