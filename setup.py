#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup

setup(
    name='Christofides',
    version='0.1.0',
    author='Duvvuri Surya Rahul',
    author_email='dsrahul@outlook.com',
    packages=['Christofides'],
    url='http://pypi.python.org/pypi/Christofides/',
    license='LICENSE.txt',
    description='Christofides Algorithm for TSP.',
    long_description=open('README.txt').read(),
    install_requires=[
    	"scipy >= 0.13.3",
        "networkx >= 1.11rc1",
		"numpy >= 1.8.2",
		"munkres >= 1.0.7"		
    ],
)
