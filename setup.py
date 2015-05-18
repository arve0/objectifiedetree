#!/usr/bin/env python

import os
import sys
from setuptools import setup

os.system('make rst')
try:
    readme = open('README.rst').read()
except FileNotFoundError:
    # fallback when installing from source package
    readme = ''

setup(
    name='objectifiedetree',
    version=open(os.path.join('objectifiedetree', 'VERSION')).read().strip(),
    description='Dot notation for ElementTrees',
    long_description=readme,
    author='Arve Seljebu',
    author_email='arve.seljebu@gmail.com',
    url='https://github.com/arve0/objectifiedetree',
    packages=[
        'objectifiedetree',
    ],
    package_dir={'objectifiedetree': 'objectifiedetree'},
    package_data={'objectifiedetree': ['VERSION']},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='objectifiedetree',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
