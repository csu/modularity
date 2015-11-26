try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(
    name='modularity',
    version='0.0.3',
    description='A library for managing dynamic modules.',
    long_description=long_description,
    author='Christopher Su',
    author_email='chris+py@christopher.su',
    url='https://github.com/csu/modularity',
    packages=['modularity']
)