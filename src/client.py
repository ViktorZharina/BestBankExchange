#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author Viktor Zharina <viktorz1986@gmail.com>
# CC-BY-SA License

import tornado.ioloop
import tornado.web
from banks import *
import json
from McBase import McBase
from decimal import *
getcontext().prec = 4

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        mc = McBase()
        table = ''
        #print mc.get('0')
        table = u'<table><tr><td>Банк</td><td>UsdBuy</td><td>UsdSell</td><td>EurBuy</td><td>EurSell</td></tr>'
        for bank_id, v in enumerate(url_bank_info):
            table += self.get_table(v, mc.get(str(bank_id)))

        table += u'</table>'
        self.write(table)

    def get_table(self, bank, data):
        table = ''
        if (data):
            exchange_rate = json.loads(data)
            table += u'<tr><td>'+bank+u'</td><td>'+exchange_rate['usd_buy']+u'</td><td>'+exchange_rate['usd_sell']+u'</td><td>'+exchange_rate['eur_buy']+u'</td><td>'+exchange_rate['eur_sell']+u'</td></tr>'
        return table

application = tornado.web.Application([
    (r"/", IndexHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()