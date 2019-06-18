#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-mavenlink',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Mavenlink API',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_mavenlink'],
      install_requires=[
          'tap-framework==0.0.4',
      ],
      entry_points='''
          [console_scripts]
          tap-mavenlink=tap_mavenlink:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_mavenlink': [
              'schemas/*.json'
          ]
      })
