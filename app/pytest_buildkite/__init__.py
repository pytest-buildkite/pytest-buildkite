# -*- coding: utf-8 -*-
"""
Pytest plugin to add Buildkite annotations for Test Results and Coverage
Reports.
"""

# System Imports
import os.path

# External Imports
from plumbum import FG, local

import pipefish

from .version import __version__

__all__ = [
    '__version__',
    'pytest_configure',
    'pytest_sessionfinish',
    'pytest_terminal_summary',
    'pytest_warning_captured',
]

DEFAULT_PATH = "test-output.xml"
DEFAULT_COV_PATH = "test-cov.xml"


def pytest_configure(config):
    """
    Allows the plugin to configure pytest, in this case we make sure the
    required reports are produced for coverage to be uploaded to Buildkite
    """
    xmlpath = config.getoption("--junitxml")
    if not xmlpath:
        config.option.xmlpath = DEFAULT_PATH

    # ensure coverage creates `xml` format
    if config.pluginmanager.has_plugin("pytest_cov"):
        config.option.cov_report["xml"] = os.path.normpath(
            os.path.abspath(
                os.path.expanduser(os.path.expandvars(
                    DEFAULT_COV_PATH
                ))
            )
        )


def pytest_sessionfinish(session, exitstatus):
    """
    Called at the completion of pytest and the report annotations are
    performed.
    """
    xmlpath = session.config.option.xmlpath

    # noqa: E501 # pylint: disable=line-too-long
    # This mirrors
    # `https://github.com/pytest-dev/pytest/blob/38adb23bd245329d26b36fd85a43aa9b3dd0406c/src/_pytest/junitxml.py#L368-L369`
    xmlabspath = os.path.normpath(
        os.path.abspath(os.path.expanduser(os.path.expandvars(xmlpath)))
    )
    if os.path.isfile(xmlabspath) and not session.shouldfail:
        markdown_msg = pipefish.process_junit_xml(xmlabspath)
        style = 'success'
        if session.testsfailed > 0:
            style = 'error'
        elif exitstatus != 0:
            style = 'warning'
        _buildkite_annotate(markdown_msg, style=style)


def pytest_terminal_summary(terminalreporter):
    """
    Coverage is finalized in the terminal summary phase.
    """
    if terminalreporter.config.pluginmanager.has_plugin("pytest_cov"):
        cov_fail_under = terminalreporter.config.option.cov_fail_under
        covpath = os.path.normpath(
            os.path.abspath(os.path.expanduser(os.path.expandvars(
                DEFAULT_COV_PATH
            )))
        )
        if os.path.exists(covpath):
            cov_style = 'success'
            if cov_fail_under is not None:
                cov_percent = pipefish.get_coverage_from_cobertura_xml(covpath)
                if cov_percent < cov_fail_under:
                    cov_style = 'error'
            markdown_msg = pipefish.process_cobertura_xml(
                covpath, cov_fail_under
            )
            _buildkite_annotate(markdown_msg, style=cov_style)
        else:
            _buildkite_annotate(
                'Coverage XML not produced {0}'.format(
                    covpath,
                ),
                style='warning',
            )


def pytest_warning_captured(  # pylint: disable=unused-argument
        warning_message, when, *args):
    """
    Raise any pytest warnings to Buildkite.
    """
    _buildkite_annotate(
        str(warning_message.message), style='warning',
    )


def _buildkite_annotate(content, style='success', context=None):
    """
    Call out to the buildkite-agent to pass a build annotation.
    """
    if context is None:
        context = 'ctx-%s' % (style,)
    agent = local['buildkite-agent']
    _ = agent[
        'annotate', content, '--style', style,
        '--context', context, '--append',
    ] & FG
