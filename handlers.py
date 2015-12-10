# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
import json
from models import cur, format_records_to_json, Index

__author__ = 'zhouqi'

version = 'item_api: 0.0.1'


class BaseHandler(RequestHandler):
    def data_received(self, chunk):
        pass


def get_info_from_raw(raw):
    return Index().get(raw)
    # return (1, 1)

class DefaultHandler(BaseHandler):
    def get(self):
        self.write(dict(version=version))

    def post(self):
        self.write(dict(version=version))


class UserItemListHandler(BaseHandler):
    def get(self, user_id):
        user_id = int(user_id)
        fields = ['item_id', 'item_name', 'item_desc', 'item_price']
        sql_fields = ['b.%s' % e for e in fields]
        sql = 'select %s from user_items a, items b where a.item_id=b.item_id and a.user_id=%d'
        cur.execute(sql % (', '.join(sql_fields), user_id))
        result = format_records_to_json(fields, cur.fetchall())
        self.write({'items': result})


class UserItemHandler(BaseHandler):
    def get(self, user_id, item_id):
        user_id = int(user_id)
        item_id = int(item_id)
        fields = ['item_id', 'item_name', 'item_desc', 'item_price']
        sql_fields = ['b.%s' % e for e in fields]
        sql = 'select %s from user_items a, items b where a.item_id=b.item_id and a.user_id=%d and a.item_id=%d'
        cur.execute(sql % (', '.join(sql_fields), user_id, item_id))
        result = format_records_to_json(fields, cur.fetchall())
        self.write(result[0])


class UserItemRawHandler(BaseHandler):
    def get(self, raw):
        info = get_info_from_raw(raw)
        if info is None:
            self.set_status(404)
        else:
            item_id, user_id = info[:2]
            fields = ['item_id', 'item_name', 'item_desc', 'item_price']
            sql_fields = ['b.%s' % e for e in fields]
            sql = 'select %s from user_items a, items b where a.item_id=b.item_id and a.user_id=%d and a.item_id=%d'
            cur.execute(sql % (', '.join(sql_fields), user_id, item_id))
            result = format_records_to_json(fields, cur.fetchall())
            self.write(result[0])
