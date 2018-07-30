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
import sys
import logging


__version__ = '1.0.0'
__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__copyright__ = 'Copyright (C) 2018 MoD-i. All rights reserved.'
__license__ = 'Distributed under terms of the MIT license.'


logger = logging.getLogger(__name__)

HOSTNAME = socket.gethostname()
USER = getpass.getuser()
COUNT = 0
SUFFIX = 'node'
HOME_DIR = str(Path.home())
BASE_NAME = f'{HOSTNAME}-{USER}-{SUFFIX}'
NODE_NAME = f'{BASE_NAME}{COUNT}'
NODE_DIR = os.path.join(HOME_DIR, NODE_NAME)
REGEX = re.escape(BASE_NAME) + r'[0-9]+'
RE_OBJ = re.compile(REGEX, re.IGNORECASE)
EXISTING_NODES = []


##
# check if all-ready a MoD-i created default node present 
# default node name: {hostname}-{count}-node
##

def check_node():
    found = 0

    for dirs in os.listdir(HOME_DIR):
        if RE_OBJ.match(dirs):
            found += 1
            EXISTING_NODES.append(dirs)
    return found 


def create_node():
    if len(EXISTING_NODES) > 0:
        logger.warning('Creating another node.')
        last_node_no = max(map(lambda node: int(node[-1]), EXISTING_NODES))
        new_node_no = last_node_no + 1
        os.mkdir(os.path.join(HOME_DIR, BASE_NAME + str(new_node_no)))
        NODE_DIR = str(os.path.join(HOME_DIR, BASE_NAME + str(new_node_no)))
    else:
        logger.warning('Creating new node.')
        os.mkdir(NODE_DIR)

    
def connect_node():
    print('command\n:', NODE_DIR)
    # p = subprocess.run(['multichaind', f'-datadir={NODE_DIR}', 'block-chain@13.232.100.99:2657'], shell=True, 
    p = subprocess.run(['multichaind -datadir=/home/toran/mint-ThinkPad-L440-root-node0 block-chain@13.232.100.99:2657'], shell=True, 
        stdout=subprocess.PIPE)
    res = p.stdout.decode()
    print(res)


def install_multichain():
    os.chdir('/tmp/')
    subprocess.run(['wget', 'https://www.multichain.com/download/multichain-1.0.5.tar.gz'])
    subprocess.run(['tar', '-xvzf', 'multichain-1.0.5.tar.gz'])
    os.chdir('multichain-1.0.5')
    subprocess.run(['mv', 'multichaind', 'multichain-cli', 'multichain-util', '/usr/local/bin'])



if __name__ == '__main__':
    found = check_node()
    if found==1:
        print(f'There is already {found} nodes linked to the MoD-i blockchain')
    elif found>1:
        print(f'There are already {found} nodes linked to the MoD-i blockchain')

    while True:
        user_inp = input("Do you still want to create a new node [y/n] : ")
        if user_inp.lower() in ('n', 'no'):
            logger.info('Aborted. Exiting.')
            sys.exit()
        elif user_inp.lower() in ('y', 'yes'):
            # install_multichain()
            logger.info('multichain installed')
            # create_node()
            logger.info('One node created.')
            connect_node()
            logger.info('Node connected.')
            sys.exit()
        else:
            print('Please enter a valid option')
            logger.info('Invaid option entered.')
