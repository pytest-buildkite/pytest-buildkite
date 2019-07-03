#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

${BASEDIR}/ci/in_docker/prepare.sh

MAIN_MODULE="pytest_buildkite"
MODULES=( "${MAIN_MODULE}" "test" )

cd "${BASEDIR}/app"
for PYVER in ${PYTHONVERS} ; do
  "python${PYVER}" -m flake8 "${MODULES[@]}"
  find "${MODULES[@]}" -iname \*.py -print0 | xargs -0 -n 1 "${BASEDIR}/ci/in_docker/pylint.sh" "python${PYVER}"
  "python${PYVER}" -m bandit -r "${MAIN_MODULE}"
  "python${PYVER}" -m pytest --cov-config=.coveragerc --cov-fail-under=30 "--cov=${MAIN_MODULE}"
done
echo 'Testing Complete'
