#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author Viktor Zharina <viktorz1986@gmail.com>
# code from here http://blog.echolibre.com/2009/11/memcache-and-python-getting-started/
from config.banks import *
from config.settings import *

"""
Banks class
Класс для работы с обменными курсами
"""
class BankBase():
    exchange_rates = {}

    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    """exchange_rates = {'bank_id': {'currency_operation': u'value',}}"""
    def get_all_values(self, currency, operation):
        return [val[currency+'_'+operation] for val in self.exchange_rates.values() if currency+'_'+operation in val.keys()]

    """Метод возвращает лучшую цену по заданной операции из переданных значений"""
    def get_best_value(self, operation, values):
        if (values):
            return max(values) if operation == 'buy' else min(values)
        return 0


    def get_all_best_values(self):
        v = []

        for cur in settings['currencys']:
            best_buy = self.get_best_value('buy', self.get_all_values(cur, 'buy'))
            v.append(best_buy)
            best_sell = self.get_best_value('sell', self.get_all_values(cur, 'sell'))
            v.append(best_sell)
        return v

    def is_best_value(self, value, currency, operation):
        all_val = get_all_values(currency, operation)
        best_val = self.get_best_value(operation, all_val)

        return True if (value == best_val) else False

    def get_bank_by_value(self, value):
        for bank_id, val in self.exchange_rates.items():
            return bank_id if value in val.values() else '0'

    def get_bank_for_exchange(self):
        bank = {}

        for cur in settings['currencys']:
            best_buy = self.get_best_value('buy', self.get_all_values(cur, 'buy'))
            best_sell = self.get_best_value('sell', self.get_all_values(cur, 'sell'))
            bank['from_' + cur] = best_buy
            bank['to_' + cur] = best_sell

        return bank

if __name__ == '__main__':
    pass