# -*- coding: utf-8 -*-
from datetime import datetime, date
from decimal import Decimal
import json
import os
from hashlib import md5

import psycopg2
import leveldb

from settings import db_host, db_name, db_user, db_password, db_port

__author__ = 'zhouqi'

db = psycopg2.connect("dbname='%s' user='%s' password='%s' host='%s' port=%d"
                      % (db_name, db_user, db_password, db_host, db_port))
cur = db.cursor()


def ensure_type(obj):
    """
    确保对象能被json序列化
    :param obj: 对象
    :return: 可被json序列化的对象
    """
    if obj.__class__ is datetime:
        return obj.isoformat().split('.')[0] + '.000Z'
    elif obj.__class__ is date:
        return str(obj)
    elif obj.__class__ is Decimal:
        return str(obj)
    else:
        return obj


def format_records_to_json(fields, res, aliases=None):
    """
    format pg records to json obj
    :param fields:query fields
    :param res: pg records
    :param aliases: json field alias
    :return: [{}, ... {}]
    """

    def _to_alias(aliases, i, default):
        if aliases is None or len(aliases) <= i or aliases[i] is None:
            return default
        else:
            return aliases[i]

    result = []
    for row in res:
        result.append(
            dict([(_to_alias(aliases, index, field), ensure_type(row[index]))
                  for index, field in enumerate(fields)]))
    return result


class BaseModel(object):
    pass


class Item(BaseModel):
    pass


class User(BaseModel):
    pass


class Index(object):
    _instance = None
    _db = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            path = './db/ldb/'
            if not os.path.exists(path):
                os.mkdir(path)
            cls._instance = super(Index, cls).__new__(cls, *args, **kwargs)
            cls._db = leveldb.LevelDB(path + '/indexdb')
        return cls._instance

    def set(self, obj):
        key = self.hash(obj.__str__())
        while self._get_from_ldb(key) is not None:
            key = self.hash(key)
        self._db.Put(key, self._encode(obj))
        return key

    def _get_from_ldb(self, key):
        try:
            return self._db.Get(key)
        except KeyError:
            return None

    def get(self, raw):
        try:
            content = self._db.Get(raw)
        except KeyError:
            content = None
        if content is not None:
            return self._decode(content)
        else:
            return None

    def update(self, raw, obj):
        try:
            content = self._db.Get(raw)
        except KeyError:
            content = None
        if content is not None:
            self._db.Put(raw, self._encode(obj))
            return True
        else:
            return False

    def hash(self, str):
        # need use base62 or base58
        return md5('\x00' + str).hexdigest()[:6]

    def _decode(self, encoded_content):
        # use json for save dev time, can use binary struct to save it
        return json.loads(encoded_content)

    def _encode(self, obj):
        # use json for save dev time, can use binary struct to save it
        return json.dumps(obj)
