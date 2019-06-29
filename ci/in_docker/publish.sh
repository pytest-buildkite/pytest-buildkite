#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "${THISDIR}" )"

cd "${BASEDIR}/app"
rm -rf dist build
python setup.py bdist_wheel sdist
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
python -m twine upload dist/*
