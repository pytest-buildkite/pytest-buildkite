#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setuptool Distribution for pytest_buildkite
"""

# {{{ Import
# System  Imports
import codecs
import os

# External Imports
from setuptools import setup

# }}}


def read(fname):
    """
    Read the contents of relative file.
    """
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-buildkite',
    version='0.1.6dev0',
    author='Tim Gates',
    author_email='tim.gates@iress.com',
    maintainer='Tim Gates',
    maintainer_email='tim.gates@iress.com',
    license='MIT',
    url='https://pytest-buildkite.github.io/index.html',
    description=(
        'Plugin for pytest that automatically publishes coverage and'
        ' pytest report annotations to Buildkite.'
    ),
    long_description=read('README.rst'),
    packages=['pytest_buildkite'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['pytest>=3.5.0', 'plumbum'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
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
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'buildkite = pytest_buildkite',
        ],
    },
)
