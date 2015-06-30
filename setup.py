#!/usr/bin/env python

# Python
import os
import sys

# Setuptools
from setuptools import setup

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name='ssl-opt-out',
    version='0.9.0',
    author='Chris Church',
    author_email='chris@ninemoreminutes.com',
    description='Opt-out of Python SSL certificate verification.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst'),
                          'rb').read().decode('utf-8'),
    license='BSD',
    keywords='python ssl',
    url='https://github.com/cchurch/ssl-opt-out',
    py_modules=['ssl_opt_out'],
    data_files=[('', ['ssl_opt_out.pth'])],
    include_package_data=False,
    zip_safe=False,
    install_requires=[],
    setup_requires=[],
    tests_require=['six'],
    test_suite='test_ssl_opt_out.suite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
    options={
        'egg_info': {
            'tag_build': '.dev',
        },
        'aliases': {
            'dev_build': 'egg_info sdist',
            'release_build': 'egg_info -b "" -R sdist',
        },
    },
    **extra
)
