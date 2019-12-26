#!/usr/bin/env python3
from setuptools import setup

__author__ = 'MuhBayu <bnugraha00@gmail.com>'
__version__ = '0.0.1'
__description__ = "Unofficial OVO Payment API SDK"

packages = [
    'ovopy',
]

install_requires = [
	'httpx',
	'pytz',
]

setup(
    name='ovopy',
    version=__version__,
    author=__author__,
    author_email='bnugraha00@gmail.com',
    license='MIT',
    url='https://github.com/MuhBayu/ovopy',
    install_requires=install_requires,
    description=__description__,
    packages=packages,
    classifiers=[
        "Programming Language :: Python",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
    ]
)