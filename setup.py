#!/usr/bin/env python
# Copyright (C) 2019 SignalFx, Inc. All rights reserved.
from setuptools.command.test import test as TestCommand
from setuptools import setup
import sys
import os


class PyTest(TestCommand):

    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)

    def run_tests(self):
        import pytest
        sys.exit(pytest.main('tests'))


cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, 'README.md')) as readme_file:
    long_description = readme_file.read()

# Keep these separated for tox extras
test_requirements = ['mock', 'pytest']

setup(
    name='OpenTracing-Patches',
    version='0.1.0',
    url='http://github.com/signalfx/opentracing-python-patches',
    download_url='http://github.com/signalfx/opentracing-python-patches/tarball/master',
    author='SignalFx, Inc.',
    author_email='info@signalfx.com',
    description='SignalFx\'s OpenTracing Patches',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['opentracing_patches'],
    platforms='any',
    license='Apache Software License v2',
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8'
    ],
    install_requires=[],
    tests_require=test_requirements,
    extras_require=dict(
        unit_tests=test_requirements,
    ),
    cmdclass=dict(test=PyTest)
)
