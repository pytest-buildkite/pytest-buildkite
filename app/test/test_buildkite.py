# -*- coding: utf-8 -*-
"""
Test cases for pytest_buildkite
"""


def test_bar_fixture(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_sth():
            assert 1 == 1
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_sth PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0  # nosec


def test_warning_output(testdir):
    """
    Raise a warning during a test and check output
    """
    # create a temporary pytest test module
    testdir.makepyfile("""
        import warnings
        def test_warnings():
            assert 1 == 1
            warnings.warn("Checking the warning feature inside a test")
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_warnings PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0  # nosec
