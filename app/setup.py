"""
Setuptool Distribution for pytest_buildkite
"""
from setuptools import setup

setup(
    name='pytest-buildkite',
    version='0.1.2dev0',
    author='Tim Gates',
    author_email='tim.gates@iress.com',
    packages=['pytest_buildkite',],
    license='MIT',
    long_description=(
        'Plugin for pytest that automatically publishes coverage and'
        ' pytest report annotations to Buildkite.'
    ),
    url='https://pytest-buildkite.github.io/index.html',
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
)
