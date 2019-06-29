#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "${BASEDIR}"

for PYVER in ${PYTHONVERS} ; do
  cd "${BASEDIR}/pipenv/${PYVER}"
  "python${PYVER}" -m pipenv install --deploy --system 
done
