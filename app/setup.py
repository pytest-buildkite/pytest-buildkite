#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
`setuptools` Distribution for pymodulenamegoeshere
"""

# {{{ Import
# System  Imports
import codecs
import os
import re

# External Imports
from setuptools import setup

# }}}

PACKAGE_NAME = 'pymodulenamegoeshere'


def load_readme(fname):
    """
    Read the contents of relative `README` file.
    """
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with codecs.open(file_path, encoding='utf-8') as fobj:
        sub = (
            '(https://github.com/'
            'yourgithuborggoeshere/yourgithubrepogoeshere'
            '/blob/master/\\g<1>)'
        )
        markdown_fixed = re.sub(
            '[(]([^)]*[.](?:md|rst))[)]',
            sub,
            fobj.read(),
        )
        rst_fixed = re.sub(
            '[(]([^)]*[.](?:md|rst))[)]',
            '^[.][.] [_][`][^`]*[`][:] ([^)]*[.](?:md|rst))',
            sub,
            markdown_fixed
        )
        return rst_fixed


def read_version():
    """
    Read the contents of relative file.
    """
    file_path = os.path.join(
        os.path.dirname(__file__), PACKAGE_NAME, 'version.py'
    )
    regex = re.compile('__version__ = [\'\"]([^\'\"]*)[\'\"]')
    with codecs.open(file_path, encoding='utf-8') as fobj:
        for line in fobj:
            mobj = regex.match(line)
            if mobj:
                return mobj.group(1)
    raise Exception('Failed to read version')


setup(
    name=PACKAGE_NAME,
    version=read_version(),
    author='yournamegoeshere',
    author_email='youremailgoeshere',
    maintainer='yournamegoeshere',
    maintainer_email='youremailgoeshere',
    packages=[PACKAGE_NAME],
    license='GPLv3+',
    description=(
        'descriptiongoeshere'
    ),
    long_description=load_readme('README.md'),
    long_description_content_type='text/markdown',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[],
    url='homepageurlgoeshere',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
