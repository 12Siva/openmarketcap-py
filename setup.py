#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To use a consistent encoding
from os import path
from codecs import open
# Always prefer setuptools over distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'openmarketcap-py',
    packages = ['openmarketcap', 'tests'],
    version = '1.0.0',
    description = 'Python wrapper around the coinmarketcap.com API.',
    author = '12Siva',
    url = 'https://github.com/12Siva/openmarketcap-py',
    project_urls={
        'Bug Reports': 'https://github.com/12Siva/openmarketcap-py/issues'
    },
    license = 'Apache v2.0 License',
    install_requires=[
    'requests>=2.18.4',
    'requests_cache>=0.4.13'
    ],
    keywords = ['cryptocurrency', 'API', 'openmarketcap','BTC', 'Bitcoin', 'LTC', 'Litecoin', 'XRP', 'Ripple', 'ETH', 'Ethereum '],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description = long_description,
    long_description_content_type='text/markdown',
)