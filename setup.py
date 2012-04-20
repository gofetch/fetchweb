from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fetchmusic',
    version='0.0.1',
    description='Flask app for Fetch Music',
    long_description=readme,
    author='Fetch',
    author_email='JubBoy333+fetch@gmail.com',
    url='https://github.com/gofetch/fetchmusic',
    license=license,
    packages=find_packages(exclude('tests', 'docs'))
)
