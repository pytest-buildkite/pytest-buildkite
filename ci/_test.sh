#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "${THISDIR}" )"

MAIN_MODULE="pyruncompare"
MODULES=( "${MAIN_MODULE}" "test" )

cd "${BASEDIR}/app"
python -m flake8 "${MODULES[@]}"
python -m pylint "${MODULES[@]}"
python -m bandit -r "${MAIN_MODULE}"
python -m pytest --cov-config=.coveragerc --cov-fail-under=100 "--cov=${MAIN_MODULE}"
echo 'Testing Complete'
