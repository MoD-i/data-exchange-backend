#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Toran Sahu <toran.sahu@yahoo.com>
#
# Distributed under terms of the MIT license.

"""

"""
import json
import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

try:
    from utils import hex_to_file, file_to_hex, char_to_hex, hex_to_char, dict_to_hex, json_to_hex, hex_to_dict, hex_to_json
except:
    from src.utils import hex_to_file, file_to_hex, char_to_hex, hex_to_char, dict_to_hex, json_to_hex, hex_to_dict, hex_to_json

##
# dict
##
d = {"key": "value", "a": 123}
h = dict_to_hex(d)
if d == hex_to_dict(h):
    print("dict passed")
else:
    print("dict failed")

##
# string
##

h = '7a61626364'
c = hex_to_char(h)
if char_to_hex(c) == h:
    print("char passed")
else:
    print("char failed")


##
# json
##
j = json.dumps(d, indent=4)
h = json_to_hex(j)
if j == hex_to_json(h):
    print("json passed")
else:
    print("json passed")
