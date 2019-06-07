from setuptools import setup

setup(
    name='pyruncompare',
    version='0.1dev',
    packages=['pyruncompare',],
    license='GPLv3+',
    long_description=(
        'Execute a python module or function and log all'
        ' calls and locals to formats that can be compared'
        ' for execution variations.'
    ),
)
