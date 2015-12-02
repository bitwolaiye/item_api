# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
import json

__author__ = 'zhouqi'

version = 'item_api: 0.0.1'


class BaseHandler(RequestHandler):
    def data_received(self, chunk):
        pass


class DefaultHandler(BaseHandler):
    def get(self):
        self.write(dict(version=version))

    def post(self):
        self.write(dict(version=version))
