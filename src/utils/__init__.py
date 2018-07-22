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
    n = 2
    line  = hexa
    hex_pair = [line[i:i+n] for i in range(0, len(line), n)]
    ascii_pair = list(map(lambda x: int(x, 16), hex_pair))
    return ''.join(list(map(chr,ascii_pair)))

def char_to_hex(char):
    # TODO
    pass

def json_to_hex(char):
    # TODO
    pass

def hex_to_json(char):
    # TODO
    pass
