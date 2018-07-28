#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-07-27 21:37

"""
auto_node_create.py
"""

import os
import subprocess
import requests
import socket
import getpass
from pathlib import Path
import re


__version__ = '1.0.0'
__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__copyright__ = 'Copyright (C) 2018 MoD-i. All rights reserved.'
__license__ = 'Distributed under terms of the MIT license.'


HOSTNAME = socket.gethostname()
USER = getpass.getuser()
COUNT = 0
SUFFIX = 'node'
PARENT_DIR = str(Path.home())
BASE_DIR = f'{HOSTNAME}-{USER}-{SUFFIX}'
NODE_DIR = f'{BASE_DIR}-{COUNT}'.lower()
# REGEX = re.escape(BASE_DIR) + r'-[0-9]+\Z'
REGEX = re.escape(BASE_DIR) + r'-[0-9]+\Z'
RE_OBJ = re.compile(REGEX)

print(os.listdir())
##
# check if all-ready a MoD-i created default node present 
# default node name: {hostname}-{count}-node
##


p = subprocess.run(['multichaind', '--help'], shell=True, 
        stdout=subprocess.PIPE)

res = p.stdout.decode()

# print("\nResult:\n", res)    
