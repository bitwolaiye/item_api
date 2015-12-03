# -*- coding: utf-8 -*-
import os
from tornado import web
from tornado.ioloop import IOLoop
from handlers import DefaultHandler, UserItemHandler
from settings import app_port, url_pre

__author__ = 'zhouqi'

routs = [
    # (r"/api/v1/job", DefaultHandler),
    # (r"/api/v1/job/([0-9a-zA-Z_-]+)", JobDetailHandler),
    # (r"/api/v1/job/([0-9a-zA-Z_-]+)/run", JobRunHandler),
    # (r"/api/v1/job/([0-9a-zA-Z_-]+)/run/([0-9]+)", JobRunDetailHandler),
    # (r"/api/v1/jenkins/notify", JenkinsNotifyHandler),
    (r"/api/v1/user/([0-9]+)/item", UserItemHandler),
    (r"/", DefaultHandler),
]

new_routs = []
for r in routs:
    new_routs.append(tuple([url_pre + r[0]] + list(r[1:])))

application = web.Application(new_routs, debug=True)

if __name__ == "__main__":
    with open('pid', 'w') as f:
        f.write(str(os.getpid()))
    application.listen(app_port)
    IOLoop.instance().start()
