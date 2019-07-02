#!/bin/bash

set -euxo pipefail
PYTHON="${1}"
TARGET="${2}"
if ! "${PYTHON}" -m pylint "${2}" ; then
   echo "Pylint failed on ${2}" >&2
   exit 1
fi
