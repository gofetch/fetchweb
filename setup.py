from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fetchweb',
    version='0.0.1',
    description='Web Frontend for Fetch',
    long_description=readme,
    author='Fetch',
    author_email='JubBoy333+fetch@gmail.com',
    url='https://github.com/gofetch/fetchweb',
    license=license,
    packages=['fetchweb'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
