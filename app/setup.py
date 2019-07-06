#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setuptool Distribution for pymodulenamegoeshere
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
    name='pymodulenamegoeshere',
    version='0.1.1dev',
    author='yournamegoeshere',
    author_email='youremailgoeshere',
    maintainer='yournamegoeshere',
    maintainer_email='youremailgoeshere',
    packages=['pymodulenamegoeshere'],
    license='GPLv3+',
    description=(
        'descriptiongoeshere'
    ),
    long_description=read('README.md'),
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
