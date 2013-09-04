#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author Viktor Zharina <viktorz1986@gmail.com>
# CC-BY-SA License

import tornado.ioloop
import tornado.web
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

        table = self.get_table(ex_rates)
        self.write(table)

    def get_table(self, ex_rates):
        #print ex_rates, type(ex_rates)
        bank = BankBase(ex_rates)
        all_best_values = bank.get_all_best_values()

        table = u"""<table><tr><td>Банк</td><td colspan=2 align="center">USD</td><td colspan=2 align="center">EUR</td></tr>
                    <tr><td></td><td>Покупка</td><td>Продажа</td><td>Покупка</td><td>Продажа</td></tr>"""

        for bank_id, v in ex_rates.items():
            best_values = list(set(v.values()) & set(all_best_values))
            usd_buy = v['usd_buy']
            usd_sell = v['usd_sell']
            eur_buy = v['eur_buy']
            eur_sell = v['eur_sell']

            table += u'<tbody><tr><td>'+url_bank_info[bank_id]+u'</td>'

            if usd_buy in best_values:
                table += '<td><b>'+usd_buy+u'</b></td>'
            else:
                table += '<td>'+usd_buy+u'</td>'

            if usd_sell in best_values:
                table += '<td><b>'+usd_sell+u'</b></td>'
            else:
                table += '<td>'+usd_sell+u'</td>'

            if eur_buy in best_values:
                table += '<td><b>'+eur_buy+u'</b></td>'
            else:
                table += '<td>'+eur_buy+u'</td>'

            if eur_sell in best_values:
                table += '<td><b>'+eur_sell+u'</b></td>'
            else:
                table += '<td>'+eur_sell+u'</td>'

        table += u'</tbody></table>'
        return table

application = tornado.web.Application([
    (r"/", IndexHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()