# -*- coding: utf-8 -*-
import os
from tornado import web
from tornado.ioloop import IOLoop
from handlers import DefaultHandler
from settings import app_port

__author__ = 'zhouqi'

application = web.Application([
    # (r"/api/v1/job", DefaultHandler),
    # (r"/api/v1/job/([0-9a-zA-Z_-]+)", JobDetailHandler),
    # (r"/api/v1/job/([0-9a-zA-Z_-]+)/run", JobRunHandler),
    # (r"/api/v1/job/([0-9a-zA-Z_-]+)/run/([0-9]+)", JobRunDetailHandler),
    # (r"/api/v1/jenkins/notify", JenkinsNotifyHandler),
    # (r"/api/v1/callback/sample", CallbackSampleHandler),
    (r"/", DefaultHandler),
], debug=True)

if __name__ == "__main__":
    with open('pid', 'w') as f:
        f.write(str(os.getpid()))
    application.listen(app_port)
    IOLoop.instance().start()
