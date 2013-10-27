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
    """ курсы валют """
    exchange_rates = {}

    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def get_all_values(self, currency, operation):
        """
        Метод возвращает все значения по валютам и типам операций. Пример:
        exchange_rates = {'bank_id': {'currency_operation': u'value',}}
        """
        return [val[currency+'_'+operation] for val in self.exchange_rates.values() if currency+'_'+operation in val.keys()]

    def get_best_value(self, operation, values):
        """
        Метод возвращает лучшую цену по заданной операции из переданных значений values
        """
        if (values):
            return max(values) if operation == 'buy' else min(values)
        return 0

    def get_all_best_values(self):
        """
        Метод возвращает список лучших курсов (макс. покупку и мин продажу)
        """
        v = []

        for cur in settings['currencys']:
            best_buy = self.get_best_value('buy', self.get_all_values(cur, 'buy'))
            v.append(best_buy)
            best_sell = self.get_best_value('sell', self.get_all_values(cur, 'sell'))
            v.append(best_sell)
        return v

    def is_best_value(self, value, currency, operation):
        """
        Метод проверяет является ли значение курса лучшим
        """
        all_val = get_all_values(currency, operation)
        best_val = self.get_best_value(operation, all_val)

        return True if (value == best_val) else False

    def get_bank_by_value(self, value):
        """
        Метод возвращает ид банка по значению курса
        """
        for bank_id, val in self.exchange_rates.items():
            return bank_id if value in val.values() else '0'

    def get_bank_for_exchange(self):
        """
        Метод возвращает словарь 
        """
        bank = {}

        for cur in settings['currencys']:
            best_buy = self.get_best_value('buy', self.get_all_values(cur, 'buy'))
            best_sell = self.get_best_value('sell', self.get_all_values(cur, 'sell'))
            bank['from_' + cur] = best_buy
            bank['to_' + cur] = best_sell

        return bank

if __name__ == '__main__':
    pass