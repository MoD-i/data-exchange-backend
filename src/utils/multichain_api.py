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
    from utils import hex_to_file, file_to_hex, char_to_hex, hex_to_char, dict_to_hex, json_to_hex, hex_to_dict, hex_to_json

except:
    from src.utils import hex_to_file, file_to_hex, char_to_hex, hex_to_char, dict_to_hex, json_to_hex, hex_to_dict, hex_to_json


__version__ = '1.0.0'
__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__copyright__ = 'Copyright (C) 2018 Clarion IT Pvt. Ltd. All rights reserved'

##
# local node
##

# rpcuser = 'multichainrpc'
# rpcpasswd = '8DtJkTWgJnHDbKNZdFuVyWo1LHFkwoKSZ3S45UyQV3AM'
# rpchost = 'localhost'
# rpcport = '6820'
# chainname = 'mychain'

##
# toran's aws node
##

rpcuser = 'multichainrpc'
rpcpasswd = '3H8Bpi3ejkWoP59Ntp7fq888jD83NvMAAyLKt29jBVu4'
# rpchost = '13.232.100.99'
rpchost = '54.72.42.143'
rpcport = '8358'
chainname = 'cg-chain'


api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

def publish_stream(stream, key, data, data_format='char'):
    if data_format == 'file':
        hex_data = file_to_hex(data) 
        txid = api.publish(stream, key, hex_data)
    elif data_format == 'json':
        hex_data = json_to_hex(data)
        txid = api.publish(stream, key, hex_data)
    elif data_format == 'dict':
        hex_data = dict_to_hex(data)
        txid = api.publish(stream, key, hex_data)
    else:
        hex_data = char_to_hex(data)
        txid = api.publish(stream, key, data)
    return txid


def get_tx_data(txid):
    hex_data = api.gettxoutdata(txid, 0)
    return hex_data

