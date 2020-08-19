# Setup script for installing the srnn_pfc package -- tools and utilities shared among notebooks.
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the version number from the version file
# Versions should comply with PEP440.  For a discussion on single-sourcing
# the version across setup.py and the project code, see
# https://packaging.python.org/en/latest/single_source_version.html
__version__ = None
with open(os.path.join(here, 'srnn_pfc', 'version.py')) as f:
    exec(f.read())  # Overwrites __version__

setup(
    name='srnn_pfc',
    version=__version__,
    description='Python interface to the Lab Streaming Layer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/neuromorphs/grill-srnn-pfc',
    author='Chadwick Boulay',
    author_email='chadwick.boulay@gmail.com',
    license='MIT',
    packages=find_packages()
)
