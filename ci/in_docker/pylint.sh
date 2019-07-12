#!/bin/bash

set -euxo pipefail
<<<<<<< HEAD
PYTHON="${1}"
TARGET="${2}"
if ! "${PYTHON}" -m pylint "${2}" ; then
=======

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

PYTHON="${1}"
TARGET="${2}"
if ! "${PYTHON}" -m pylint --rcfile "${BASEDIR}/app/.pylintrc" "${2}" ; then
>>>>>>> d6e2066bc7dfe5a9e7daeb0d7a6cd1ce438b42a5
   echo "Pylint failed on ${2}" >&2
   exit 1
fi
