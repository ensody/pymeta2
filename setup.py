from setuptools import setup, find_packages

DESCRIPTION = 'Parser generator'

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

setup(name='pymeta2',
      packages=find_packages(exclude=('tests', 'tests.*')),
      author='Waldemar Kornewald',
      url='http://www.allbuttonspressed.com/projects/pymeta2',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      install_requires=[],
)
