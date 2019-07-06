#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

source ${BASEDIR}/ci/in_docker/prepare.sh

cd "${BASEDIR}/app"
for PYVER in ${PYTHONVERS} ; do
  "python${PYVER}" -m flake8 "${MODULES[@]}"
  find "${MODULES[@]}" -iname \*.py -print0 | xargs -0 -n 1 "python${PYVER}" -m pylint
  "python${PYVER}" -m bandit -r "${MODULES[@]}"
  "python${PYVER}" -m pytest --cov-config=.coveragerc --cov-fail-under=100 "--cov=${MAIN_MODULE}"
  "python${PYVER}" -m isort -rc -c "${MODULES[@]}"
done
echo 'Testing Complete'
