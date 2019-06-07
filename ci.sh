#!/bin/bash

set -euxo pipefail

if ! which make ; then
    echo 'GNU Make is missing!' >&2
    exit 1
fi
if ! which docker ; then
    echo 'Docker is missing!' >&2
    exit 1
fi
if ! which docker-compose ; then
    echo 'Docker-Compose is missing!' >&2
    exit 1
fi
make build
