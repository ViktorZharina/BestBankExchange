#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author Viktor Zharina <viktorz1986@gmail.com>
# CC-BY-SA License

import tornado.ioloop
import tornado.web
import tornado.template
from config.banks import *
from config.settings import *
import json
from McBase import McBase
from BankBase import BankBase
from decimal import *
getcontext().prec = 4

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        mc = McBase()
        ex_rates = {}

        for x in xrange(len(url_bank_info)):
            ex_rates[x] = json.loads(mc.get(str(x)))

        bank = BankBase(ex_rates)
        best_values = bank.get_all_best_values()
        loader = tornado.template.Loader("templates")
        template = loader.load("index.html").generate(bank=bank, ex_rates=ex_rates, best_values = best_values, bank_info = url_bank_info)
        self.write(template)

application = tornado.web.Application([
    (r"/", IndexHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()