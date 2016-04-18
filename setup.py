#!/usr/bin/env python
from setuptools import setup
import os


# Utility function to read README file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='aashe_theme',
      version='1.10.5',
      description='Unify, themed for AASHE',
      author='AASHE',
      author_email='webdev@aashe.org',
      url='http://pypi.aashe.org/',
      long_description=read("README.md"),
      packages=['aashe_theme', ],
      include_package_data=True,
      license="Not Licensed",
      install_requires=["Django>=1.8", ],
      dependency_links=[('git+https://github.com/AASHE/')]
      )
