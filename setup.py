# -*- coding: utf-8 -*-
"""
@author: uwe
"""

import sys
import os
from setuptools import setup

setup(name='feedinlib',
      version='0.0.12',
      description='Creating time series from pv or wind power plants.',
      url='http://github.com/oemof/feedinlib',
      author='oemof developing group',
      author_email='birgit.schachler@rl-institut.de',
      license='GPL3',
      packages=['feedinlib'],
      zip_safe=False,
      install_requires=['numpy >= 1.7.0',
                        'pandas >= 0.13.1',
                        'pvlib[optional] >= 0.5.0',
                        'windpowerlib >= 0.0.6',
                        'xarray >= 0.12.0',
                        'cdsapi >= 0.1.4',
                        'scipy'])
