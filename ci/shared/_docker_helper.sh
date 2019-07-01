#!/bin/bash

function docker_compose_run() {
    USEROPT="$(id -u):$(id -g)"
    docker-compose build
    docker-compose up -d --force-recreate
    docker-compose run --rm -u "${USEROPT}" "$@"
    docker-compose down
}
