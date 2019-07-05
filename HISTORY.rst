Release History
~~~~~~~~~~~~~~~

0.2.0
-----

* Initial release - very basic markdown output to Buildkite annotations

0.1.0
-----

This repository was repurposed from tonybaloney's pytest-buildkite library.

History from pytest-azurepipelines
----------------------------------

* Add support for pytest-cov uploading coverage results and the htmlcov as an artifact
* Known issue: requires `--cov-report html` to be added on the CLI for the report upload to work
* Add `--napoleon-docstrings` flag for shortened docstrings
* Fixed bug where some nodes could not be renamed if using `conftest.py`
* Fix custom title flag #10
