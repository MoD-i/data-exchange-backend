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
    from utils import hex_to_file, file_to_hex, hex_to_char
except:
    from src.utils import hex_to_file, file_to_hex, hex_to_char

def hex_to_char(hexa):
    n = 2
    line  = hexa
    hex_pair = [line[i:i+n] for i in range(0, len(line), n)]
    ascii_pair = list(map(lambda x: int(x, 16), hex_pair))
    return ''.join(list(map(chr,ascii_pair)))


hexa = '5b7ba202020226b6579223a202276616c7565222ca202020226b657932223a202276616c75653222a7d5d'

res = hex_to_char(hexa)
print(json.dumps(res, indent=4))
