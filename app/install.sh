#!/bin/bash

set -euxo pipefail
python -m pip install pipenv
python -m pipenv install --deploy --system 

