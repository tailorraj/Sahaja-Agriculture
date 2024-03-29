# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sahaja_customization/__init__.py
from sahaja_customization import __version__ as version

setup(
	name='sahaja_customization',
	version=version,
	description='Private Customization',
	author='Raaj Tailor',
	author_email='tailorraj111@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
