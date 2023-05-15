#!/usr/bin/env python

from setuptools import setup

setup(

    name="PyTumblr",
    version="0.0.6-alpha",
    description="A Python API v2 wrapper for Tumblr",
    author="Yannick PELTIER",
    author_email="",
    url="https://github.com/yannick60/pytumblr",
    packages = ['pytumblr'],
    license = "LICENSE",

    test_suite='nose.collector',

    install_requires = [
        'oauth2',
        'httpretty'
    ],

    tests_require=[
        'nose',
        'nose-cov',
        'mock'
    ]

)
