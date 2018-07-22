#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-07-19 12:14

"""
aws_local.py
"""

from Savoir import Savoir
import json
import codecs
import binascii
import sys, os
import base64

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

try:
    from utils import hex_to_file, file_to_hex
except:
    from src.utils import hex_to_file, file_to_hex

__version__ = '1.0.0'
__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__copyright__ = 'Copyright (C) 2018 Clarion IT Pvt. Ltd. All rights reserved'



rpcuser = 'multichainrpc'
rpcpasswd = '8DtJkTWgJnHDbKNZdFuVyWo1LHFkwoKSZ3S45UyQV3AM'
rpchost = 'localhost'
rpcport = '6820'
chainname = 'mychain'

def jsonify(data):
    return json.dumps(data, indent=4)

api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

def publish_stream(stream, key, data):
    txid = api.publish(stream, key, data)
    return txid

def get_tx_data(txid):
    data = api.gettxoutdata(txid, 0)
    return data

