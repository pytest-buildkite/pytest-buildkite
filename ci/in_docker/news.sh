#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

source ${BASEDIR}/ci/in_docker/prepare.sh

PYVER=3.7
cd "${BASEDIR}"
"python${PYVER}" -m towncrier "$@"
