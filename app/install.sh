#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "${BASEDIR}"

for PYVER in ${PYTHONVERS} ; do
  cd "${BASEDIR}/pipenv/${PYVER}"
  rm -rf "${BASEDIR}/.local"
  "python${PYVER}" -m pipenv install --verbose --deploy --system --python "${PYVER}"
  rm -rf "${BASEDIR}/.local"
done
