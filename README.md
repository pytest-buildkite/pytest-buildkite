# pytest-buildkite

[![Azure Status](https://dev.azure.com/timgates/timgates/_apis/build/status/pytest-buildkite.pytest-buildkite?branchName=master)](https://dev.azure.com/timgates/timgates/_build/latest?definitionId=11&branchName=master)
[![Travis Status](https://travis-ci.org/pytest-buildkite/pytest-buildkite.svg?branch=master)](https://travis-ci.org/pytest-buildkite/pytest-buildkite)
[![Appveyor Status](https://ci.appveyor.com/api/projects/status/nod9sis12whcv0d2/branch/master?svg=true)](https://ci.appveyor.com/project/pytest-buildkite/pytest-buildkite)
[![PyPI version](https://img.shields.io/pypi/v/pytest-buildkite.svg)](https://pypi.org/project/pytest-buildkite)
[![Python Versions](https://img.shields.io/pypi/pyversions/pytest-buildkite.svg)](https://pypi.org/project/pytest-buildkite)
[![PyPI downloads per month](https://img.shields.io/pypi/dm/pytest-buildkite.svg)](https://pypi.org/project/pytest-buildkite)
[![Documentation Status](https://readthedocs.org/projects/pytest-buildkite/badge/?version=latest)](https://pytest-buildkite.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/pytest-buildkite/pytest-buildkite/badge.svg)](https://coveralls.io/github/pytest-buildkite/pytest-buildkite/)
[![Black](https://camo.githubusercontent.com/28a51fe3a2c05048d8ca8ecd039d6b1619037326/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667)](https://github.com/psf/black)

Plugin for [pytest](https://github.com/pytest-dev/pytest)
that automatically publishes coverage and pytest report
[annotations](https://buildkite.com/docs/agent/v3/cli-annotate)
to BuildKite.

Note: This library was originally re-purposed from
[`tonybaloney's` pytest-azurepipelines](https://github.com/tonybaloney/pytest-azurepipelines)

Just run pytest with this plugin and see your test results in the BuildKite UI!

![Screenshot](https://github.com/pytest-buildkite/pytest-buildkite/raw/master/screenshot.png)


More details can be found in the
[Online Documentation.](https://pytest-buildkite.readthedocs.io/en/latest/)

# Installation

You can install pytest_buildkite for
[Python](https://www.python.org/) via
[pip](https://pypi.org/project/pip/)
from [PyPI](https://pypi.org/).

```
$ pip install pytest-buildkite
```




## Prerequisites:
- pipefish
- plumbum


## Download from PyPI.org

https://pypi.org/project/pytest-buildkite/

# Features:

- Overloads the `--junit-xml` flag on execution with a default value
- Uploads test results automatically, no need for a separate test results upload command
- Displays the number of failed tests if there were failures as an error message in the UI
- Displays summary of code coverage if pytest-cov is installed

# Running in Docker

To make the buildkite-agent available in docker make sure the agent is bind
mounted into the docker image (or installed in the container) and the
environment variables are passed down. A sample docker compose configuration
is show below.

```
environment:
  - BUILDKITE
  - BUILDKITE_AGENT_ACCESS_TOKEN
  - BUILDKITE_ARTIFACT_UPLOAD_DESTINATION
  - BUILDKITE_BRANCH
  - BUILDKITE_BUILD_ID
  - BUILDKITE_BUILD_NUMBER
  - BUILDKITE_BUILD_URL
  - BUILDKITE_COMMIT
  - BUILDKITE_ENV_FILE
  - BUILDKITE_JOB_ID
  - BUILDKITE_LABEL
  - BUILDKITE_MESSAGE
  - BUILDKITE_ORGANIZATION_SLUG
  - BUILDKITE_REPO
  - BUILDKITE_S3_ACCESS_KEY_ID
 - BUILDKITE_S3_ACCESS_URL
  - BUILDKITE_S3_ACL
  - BUILDKITE_S3_DEFAULT_REGION
  - BUILDKITE_S3_SECRET_ACCESS_KEY
  - BUILDKITE_TAG
  - CI
volumes:
  - type: bind
    source: /usr/bin/buildkite-agent
    target: /usr/bin/buildkite-agent
  - type: bind
    source: /usr/bin/buildkite-agent-original
    target: /usr/bin/buildkite-agent-original
```

# Contributing

Contributions are very welcome, consider using the
[file an issue](https://github.com/pytest-buildkite/pytest-buildkite/issues)
to discuss the work before beginning, but if you already have a Pull Request
ready then this is no problem, please submit it and it will be very gratefully
considered. The [Contribution Guidelines](CONTRIBUTING.md)
outlines the pytest-buildkite commitment to ensuring all
contributions receive appropriate recognition.

# License


Distributed under the terms of the [MIT](http://opensource.org/licenses/MIT)
license, "pytest-buildkite" is free and open source software


# Issues

If you encounter any problems, please
[file an issue](https://github.com/pytest-buildkite/pytest-buildkite/issues)
along with a detailed description.

# Additional Documentation:

* [Online Documentation](https://pytest-buildkite.readthedocs.io/en/latest/)
* [News](NEWS.rst).
* [Template Updates](COOKIECUTTER_UPDATES.md).
* [Code of Conduct](CODE_OF_CONDUCT.md).
* [Contribution Guidelines](CONTRIBUTING.md).
