from setuptools import setup, find_packages
import os

DESCRIPTION = 'Parser generator'

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

setup(name='pymeta2',
      packages=find_packages(),
      author='Waldemar Kornewald',
      url='http://www.allbuttonspressed.com/projects/pymeta2',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      install_requires=[],
)
