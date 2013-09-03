#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author Viktor Zharina <viktorz1986@gmail.com>
# CC-BY-SA License

import tornado.ioloop
import tornado.web
from banks import *
import json
import MySQLdb
from McBase import McBase
from decimal import *
getcontext().prec = 4

class IndexHandler(tornado.web.RequestHandler):
    def get(self):

        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", IndexHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()