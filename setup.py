import re

from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))
source_dir = ''  # the name of the directory containing the source, relative to "here"

# Read the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Read the version from __init__.py
version_re = r'^__version__ = [\'"]([^\'"]*)[\'"]'
init_path = path.join(here, source_dir, '__init__.py')
with open(init_path) as f:
    match = re.search(version_re, f.read(), re.MULTILINE)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError('Unable to find __version__ in {0}'.format(init_path))

setup(
    name='',
    version=version,
    
    description='',
    long_description=long_description,
    license='MIT',
    
    url='',
    author='',
    author_email='',
    
    packages=find_packages(exclude=['docs']),
    
    # install_requires=,
    # python_requires=
    
    classifiers=[
    
    ]
)
