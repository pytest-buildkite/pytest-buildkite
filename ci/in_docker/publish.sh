#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

cd "${BASEDIR}/app"
rm -rf dist build
for PYVER in ${PYTHONVERS} ; do
  "python${PYVER}" setup.py bdist_wheel
done
python3.7 setup.py sdist
python3.7 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
python3.7 -m twine upload dist/*
