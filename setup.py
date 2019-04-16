import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="outsettingsvalues",
    version="0.0.1",
    install_requires=[],
    requires=[],
    packages=["outsettingsvalues"],
    description='Some description',
    long_description=README,

)
