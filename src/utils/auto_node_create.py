#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-07-27 21:37

"""
auto_node_create.py
"""

import os
from subprocess import call
import requests


__version__ = '1.0.0'
__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__copyright__ = 'Copyright (C) 2018 MoD-i. All rights reserved.'
__license__ = 'Distributed under terms of the MIT license.'

res = call(['multichaind', '--help'])
print('ok')    
