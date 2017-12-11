from setuptools import setup, find_packages

from os import path

with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='damm',
  description='Damm checkdigit algorithm',
  long_description=readme,
  version='0.1.0',
  author='Jan Cajthaml',
  author_email='jan.cajthaml@gmail.com',
  license=license,
  keywords='damm checkdigit checksum',
  url='https://github.com/jancajthaml-python/damm',
  packages=['damm'],
  zip_safe=True,
  test_suite='tests',
  extras_require={
    'test': ['coverage'],
  },
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Topic :: Utilities"
  ],
)
