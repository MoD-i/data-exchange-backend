#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Toran Sahu <toran.sahu@yahoo.com>
#
# Distributed under terms of the MIT license.

"""
__init__.py
"""

import binascii
import json

def file_to_hex(filename):
    with open(filename, 'rb') as f:
        content = f.read()
        b = binascii.hexlify(content)
        return b.decode('utf-8')


def hex_to_file(hexa, filename):
    hexa = bytes(hexa, 'utf-8')
    with open(filename, 'wb') as f:
        data = binascii.unhexlify(hexa)
        f.write(data)


def hex_to_char(hexa):
    # return s and chr(atoi(s[:2], base=16)) + toStr(s[2:]) or ''
    n = 2
    line  = hexa
    hex_pair = [line[i:i+n] for i in range(0, len(line), n)]
    ascii_pair = list(map(lambda x: int(x, 16), hex_pair))
    return ''.join(list(map(chr,ascii_pair)))


def char_to_hex(s):
    # lst = []
    # for ch in s:
    #     hv = hex(ord(ch)).replace('0x', '')
    #     if len(hv) == 1:
    #         hv = '0'+hv
    #     lst.append(hv)
    # return reduce(lambda x,y:x+y, lst)
    return (s.encode('utf-8')).hex()


def json_to_hex(data):
    return char_to_hex(str(data))


def hex_to_json(hexa):
    dict_from_str = json.loads( hex_to_char(hexa))
    return json.dumps(dict_from_str, indent=4)


def dict_to_hex(data):
    json_from_dict = json.dumps(data, indent=4)
    return char_to_hex(str(json_from_dict))


def hex_to_dict(hexa):
    return json.loads( hex_to_char(hexa))
