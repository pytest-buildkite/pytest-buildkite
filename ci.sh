#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

CMD="${1:-test}"
USERID="$(id -u)"
export USERID

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
cd "${BASEDIR}"
make "${CMD}" "${@:2}"

