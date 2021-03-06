#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pyflightdata',
    version='0.3',
    description='Get flight data from websites by making HTTP calls',
    long_description='Please visit https://github.com/supercoderz/pyflightdata for more details',
    author='Narahari Allamraju',
    author_email='anarahari@gmail.com',
    url='https://github.com/supercoderz/pyflightdata',
    packages=['pyflightdata'],
    requires=[
        'lxml',
        'requests',
        'beautifulsoup4'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3',
    ])
