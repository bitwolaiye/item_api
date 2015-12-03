# -*- coding: utf-8 -*-
__author__ = 'zhouqi'

app_port = 8000

db_name = 'item_api'
db_user = 'item_api'
db_port = 5432
db_password = ''
db_host = '127.0.0.1'

url_pre = '/item'

settings_fields = ['db_name', 'db_user', 'db_port', 'db_password', 'db_host', 'url_pre']


def load_addition_config():
    try:
        from addition_settings import settings_dict
        for field in settings_fields:
            if field in settings_dict:
                globals()[field] = settings_dict[field]
    except ImportError as ex:
        print(ex)


load_addition_config()
