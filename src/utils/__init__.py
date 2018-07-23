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
from django.db import connection
from django.conf import settings


def jsonify(data):
    return json.dumps(data, indent=4)


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
    data = json.dumps(data)
    return char_to_hex(str(data))


def hex_to_json(hexa):
    """
    This returns LIST or DICT
    """
    # TODO
    # return hex_to_char(hexa)
    l = eval(hex_to_char(hexa))
    return l # json.dumps(l)


def dict_to_hex(data):
    json_from_dict = json.dumps(data, indent=4)
    return char_to_hex(str(json_from_dict))


def hex_to_dict(hexa):
    return json.loads( hex_to_char(hexa))


def fetch_next_id(table_name):
    db_engine = connection.settings_dict['ENGINE']

    if db_engine == 'django.db.backends.sqlite3':
        cursor = connection.cursor()
        cursor.execute(f"select seq from sqlite_sequence where name='{table_name}'")
        row = cursor.fetchone()
        cursor.close()
        # if sqlite_sequence table has record for the table_name
        if row is not None:
            seq_id = int(row[0])
        # else if its first record insertion in the table_name
        else:
            seq_id = 0
        return seq_id + 1
    elif db_engine == 'django.db.backends.mysql':
        cursor = connection.cursor()
        # database_name = 'ethereal_machines'
        database_name = settings.DATABASES['default']['NAME']
        cursor.execute(
            f"select auto_increment from information_schema.tables where auto_increment is not null and table_schema = '{database_name}' and table_name = '{table_name}'")
        row = cursor.fetchone()
        cursor.close()
        seq_id = int(row[0])
        return seq_id
    elif db_engine == 'django.db.backends.postgresql_psycopg2':
        cursor = connection.cursor()
        cursor.execute(
            "SELECT nextval('{0}_{1}_id_seq'::regclass)".format(
                instance._meta.app_label.lower(),
                instance._meta.object_name.lower(),
            )
        )
        row = cursor.fetchone()
        cursor.close()
        return int(row[0])
    elif db_engine == 'django.db.backends.oracle':
        pass
    else:
        raise


def notify(model, frm, to, ticket_no, txid, stream, key):
    obj = model.objects.create(frm=frm, to=to, ticket_no=ticket_no, txid=txid, stream=stream, key=key)
    obj.save()


