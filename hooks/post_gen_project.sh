#!/bin/bash

set -euxo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TOP="$(dirname "${BASEDIR}")"

cd "${TOP}"
rm \
  app/pytest_buildkite/__main__.py \
  app/tests/test_main.py
git checkout -- \
 NEWS.rst \
 app/pytest_buildkite \
 app/tests \
 docs/modules.rst \
 docs/setup.rst \
 docs/tests.rst \
 icon-above-font.png \
 screenshot.png \
