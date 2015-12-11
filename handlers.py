# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
import json
from apns import APNs, Frame, Payload
from models import cur, db, format_records_to_json, Index
from settings import notification_key_path, notification_cert_path

__author__ = 'zhouqi'

version = 'item_api: 0.0.1'


class BaseHandler(RequestHandler):
    def data_received(self, chunk):
        pass


def get_info_from_raw(raw):
    return Index().get(raw)


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


class UserItemOrderHandler(BaseHandler):
    def post(self, user_id, item_id):
        user_id = int(user_id)
        item_id = int(item_id)
        sql = 'select user_id,user_name from users where user_id=%d'
        cur.execute(sql % user_id)
        user = cur.fetchone()
        if user is None:
            self.set_status(404)
            return
        sql = 'select item_id, item_name,item_desc,item_price from items where item_id=%d'
        cur.execute(sql % item_id)
        item = cur.fetchone()
        if item is None:
            self.set_status(404)
            return
        sql = 'INSERT INTO orders(user_id, item_id, buy_time, item_price) VALUES (%d, %d, now(), %s) RETURNING order_id'
        cur.execute(sql % (user_id, item_id, str(item[3])))
        order_id = cur.fetchone()[0]
        raw = Index().set((item_id, user_id, order_id))
        sql = "update orders set raw='%s' where order_id=%d"
        cur.execute(sql % (raw, order_id))
        db.commit()
        self.write({'raw': raw})


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
            fields = ['order_id', 'item_price', 'buy_time']
            sql_fields = ['a.%s' % e for e in fields]
            sql = 'select %s from orders a where a.user_id=%d and a.item_id=%d'
            cur.execute(sql % (', '.join(sql_fields), user_id, item_id))
            orders = format_records_to_json(fields, cur.fetchall())
            result[0]['orders'] = orders
            self.write(result[0])


class UserItemRawShowHandler(BaseHandler):
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
            self.render("templates/order.html", title="Order", items=None)

    def post(self, raw):
        self.render("templates/order_success.html", title="Order", items=None)

class UserItemRawNotificationHandler(BaseHandler):
    def post(self, raw):
        info = get_info_from_raw(raw)
        if info is None:
            self.set_status(404)
        else:
            order_id = info[-1]
            token = self.get_argument('token')
            sql = "insert into order_devices(order_id, device_token) VALUES (%d, '%s')"
            cur.execute(sql % (order_id, token))
            db.commit()
            self.write({'result': True})

class DeviceNotificationHandler(BaseHandler):
    def post(self, token):
        content = self.get_argument('content')
        apns = APNs(use_sandbox=True, cert_file=notification_cert_path, key_file=notification_key_path)
        payload = Payload(alert=content, sound="default")
        apns.gateway_server.send_notification(token, payload)
        self.write({'result': True})


class IndexGenHandler(BaseHandler):
    def post(self, cnt):
        result = []
        for i in range(cnt):
            result.append(Index().set([]))
        self.write({'indexes': result})
