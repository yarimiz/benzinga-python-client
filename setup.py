#!/usr/bin/env python

from distutils.core import setup
import setuptools  # noqa
setup(
        name='Benzinga Data Client',
        version='0.5',
        description='Python Client Library for Benzinga Data',
        author='Benzinga Developers',
        author_email='dev@benzinga.com',
        url='https://cloud.benzinga.com',
        packages=['benzinga'],
        install_requires=['requests']
    )