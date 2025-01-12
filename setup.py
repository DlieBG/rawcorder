# -*- coding: utf-8 -*-
"""
rawcorder - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from setuptools import find_packages, setup

setup(
    name='rawcorder',
    version='0.0.1',
    description='',
    url='https://git.univ.leitwert.net/imprj/01-bgp-testbed/rawcorder',
    author='Benedikt Schwering',
    author_email='mail@bschwer.ing',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'click',
        'pika',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'rawcorder=src.main:cli',
        ],
    },
)
