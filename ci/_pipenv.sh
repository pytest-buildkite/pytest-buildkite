#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "${THISDIR}" )"

MAIN_MODULE="pymodulenamegoeshere"
MODULES=( "${MAIN_MODULE}" "test" )

cd "${BASEDIR}/app"
python -m pipenv "$@"
