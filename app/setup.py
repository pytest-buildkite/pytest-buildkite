"""
Setuptool Distribution for pymodulenamegoeshere
"""
from setuptools import setup

setup(
    name='pymodulenamegoeshere',
    version='0.1.1dev',
    author='Tim Gates',
    author_email='tim.gates@iress.com',
    packages=['pymodulenamegoeshere',],
    license='GPLv3+',
    long_description=(
        'Execute a python module or function and log all'
        ' calls and locals to formats that can be compared'
        ' for execution variations.'
    ),
    url='homepageurlgoeshere',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE V3 (GPLV3)",
        "Operating System :: OS Independent",
    ],
)
