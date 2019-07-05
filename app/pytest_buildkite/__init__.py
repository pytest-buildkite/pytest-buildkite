# -*- coding: utf-8 -*-
"""
Pytest plugin to add Builekite annotations for Test Results and Coverage
Reports.
"""

import io
import os.path
import sys

from plumbum import FG, local

DEFAULT_PATH = "test-output.xml"


def pytest_addoption(parser):
    """
    Add command line group options to pytest.
    """
    group = parser.getgroup("pytest_buildkite")
    group.addoption(
        "--test-run-title",
        action="store",
        dest="buildkite_run_title",
        default="Pytest results",
        help="Set the BuildKite test run title.",
    )
    group.addoption(
        "--napoleon-docstrings",
        action="store_true",
        dest="napoleon",
        default=False,
        help="If using Google, NumPy, or PEP 257 multi-line docstrings.",
    )


def pytest_collection_modifyitems(  # pylint: disable=unused-argument
            session, config, items
        ):
    """
    This is called after the tests have been collected and allows the plugin
    to record information against the test case
    """
    for item in items:
        # Make sure that nodes have required attributes
        if not hasattr(item, "obj") or not hasattr(item.parent, "obj"):
            continue

        parent = item.parent.obj  # Test class/module
        node = item.obj  # Test case
        if config.getoption("napoleon"):
            suite_doc = (
                parent.__doc__.split("\n\n")[0]
                if parent.__doc__ else parent.__name__
            )
            case_doc = node.__doc__.split("\n\n")[0] if node.__doc__ else None
            item._nodeid = (  # pylint: disable=protected-access
                "[{0}] {1}/{2}".format(
                    case_doc, suite_doc, item.name
                )
            )


def pytest_configure(config):
    """
    Allows the plugin to configure pytest, in this case we make sure the
    required reports are produced for coverage to be uploaded to Buildkite
    """
    xmlpath = config.getoption("--junitxml")
    if not xmlpath:
        config.option.xmlpath = DEFAULT_PATH

    # ensure coverage creates xml format
    if config.pluginmanager.has_plugin("pytest_cov"):
        config.option.cov_report["xml"] = os.path.normpath(
            os.path.abspath(
                os.path.expanduser(os.path.expandvars("test-cov.xml"))
            )
        )
        if "html" not in config.option.cov_report:
            config.option.cov_report["html"] = None


def pytest_sessionfinish(session, exitstatus):
    """
    Called at the completion of pytest and the report annotations are
    performed.
    """
    xmlpath = session.config.option.xmlpath

    # This mirrors
    # https://github.com/pytest-dev/pytest/blob
    #    /38adb23bd245329d26b36fd85a43aa9b3dd0406c/src
    #    /_pytest/junitxml.py#L368-L369
    xmlabspath = os.path.normpath(
        os.path.abspath(os.path.expanduser(os.path.expandvars(xmlpath)))
    )
    mountinfo = None
    if os.path.isfile('/.dockerenv'):
        with io.open(
                    '/proc/1/mountinfo', 'rb',
                ) as fobj:
            mountinfo = fobj.read()
        mountinfo = mountinfo.decode(sys.getfilesystemencoding())
    if mountinfo:
        xmlabspath = apply_docker_mappings(mountinfo, xmlabspath)

    # Set the run title in the UI to a configurable setting
    description = session.config.option.buildkite_run_title.replace("'", "")

    print(
        "##vso[results.publish type=JUnit;runTitle='{1}';]{0}".format(
            xmlabspath, description
        )
    )

    if exitstatus != 0 and session.testsfailed > 0 and not session.shouldfail:
        print(
            "##vso[task.logissue type=error;]{0} test(s) failed,"
            " {1} test(s) collected.".format(
                session.testsfailed, session.testscollected
            )
        )
    buildkite_annotate()

    if session.config.pluginmanager.has_plugin("pytest_cov"):
        covpath = os.path.normpath(
            os.path.abspath(
                os.path.expanduser(os.path.expandvars("test-cov.xml"))
            )
        )
        reportdir = os.path.normpath(os.path.abspath("htmlcov"))
        if os.path.exists(covpath):
            if mountinfo:
                covpath = apply_docker_mappings(mountinfo, covpath)
                reportdir = apply_docker_mappings(mountinfo, reportdir)
            print(
                "##vso[codecoverage.publish codecoveragetool=Cobertura"
                ";summaryfile={0};reportdirectory={1};]".format(
                    covpath, reportdir
                )
            )
        else:
            print(
                "##vso[task.logissue type=warning;]{0}".format(
                    "Coverage XML was not created, skipping upload."
                )
            )


def apply_docker_mappings(mountinfo, dockerpath):
    """
    Parse the /proc/1/mountinfo file and apply the mappings so that docker
    paths are transformed into the host path equivalent so Buildkite
    finds the file assuming the path has been bind mounted from the host.
    """
    for line in mountinfo.splitlines():
        words = line.split(' ')
        if len(words) < 5:
            continue
        docker_mnt_path = words[4]
        host_mnt_path = words[3]
        if dockerpath.startswith(docker_mnt_path):
            dockerpath = ''.join([
                host_mnt_path,
                dockerpath[len(docker_mnt_path):],
            ])
    return dockerpath


def pytest_warning_captured(  # pylint: disable=unused-argument
            warning_message, when, *args
        ):
    """
    Raise any pytest warnings to Buildkite.
    """
    print(
        "##vso[task.logissue type=warning;]{0}".format(
            str(warning_message.message)
        )
    )


def buildkite_annotate():
    """
    Call out to the buildkite-agent to pass a build annotation.
    """
    agent = local['buildkite-agent']
    _ = agent[
        'annotate', 'Example `success` style', '--style', 'success',
        '--context', 'ctx-success',
    ] & FG
