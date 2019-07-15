.. image:: https://github.com/pytest-buildkite/pytest-buildkite/raw/master/icon-above-font.png
    :width: 450px
    :align: center

=====================
pytest-buildkite
=====================

.. image:: https://dev.azure.com/timgates/timgates/_apis/build/status/pytest-buildkite.pytest-buildkite?branchName=master
   :target: https://dev.azure.com/timgates/timgates/_apis/build/status/pytest-buildkite.pytest-buildkite?branchName=master)](https://dev.azure.com/timgates/timgates/_build/latest?definitionId=11&branchName=master
   :alt: Build status

.. image:: https://img.shields.io/pypi/v/pytest-buildkite.svg
    :target: https://pypi.org/project/pytest-buildkite
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-buildkite.svg
    :target: https://pypi.org/project/pytest-buildkite
    :alt: Python versions

.. image:: https://img.shields.io/pypi/dm/pytest-buildkite.svg
     :target: https://pypi.python.org/pypi/pytest-buildkite/
     :alt: PyPI download month

Note: This library was repurposed from tonybaloney's pytest-azurepipelines.

Plugin for `pytest`_ that automatically publishes coverage and pytest report
`annotations`_ to BuildKite.

Just run pytest with this plugin and see your test results in the BuildKite UI!

.. image:: https://github.com/pytest-buildkite/pytest-buildkite/raw/master/screenshot.png
    :width: 600px
    :align: center

----

Features:

* Overloads the `--junit-xml` flag on execution with a default value
* Uploads test results automatically, no need for a seperate test results upload command
* Displays the number of failed tests if there were failures as an error message in the UI
* Displays summary of code coverage if pytest-cov is installed


Installation
------------

You can install "pytest-buildkite" via `pip`_ from `PyPI`_::

    $ pip install pytest-buildkite

Running in Docker
-----------------

To make the buildkite-agent available in docker make sure the agent is bind
mounted into the docker image (or installed in the container) and the
environment variables are passed down. A sample docker compose configuration
is show below.

.. code-block:: yaml

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

Contributing
------------

Contributions are very welcome, consider using the `file an issue`_ to discuss
the work before begining, but if you already have a Pull Request ready then
this is no problem, please submit it and it will be very gratefully
considered. The `Contribution Guidelines`_ outlines our commitment to ensuring
all contributions receive appropriate recognition.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-buildkite" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

Additional Documentation
------------------------
* `Code of Conduct`_
* `Contribution Guidelines`_

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/pytest-buildkite/pytest-buildkite/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
.. _`annotations`: https://buildkite.com/docs/agent/v3/cli-annotate
.. _`Code of Conduct`: CODE_OF_CONDUCT.md
.. _`Contribution Guidelines`: CONTRIBUTING.md
