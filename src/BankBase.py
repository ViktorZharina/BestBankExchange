#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author Viktor Zharina <viktorz1986@gmail.com>
# code from here http://blog.echolibre.com/2009/11/memcache-and-python-getting-started/
import memcache

"""
Banks class

Класс для работы с банками
"""
class BankBase():
    """Методы для работы с курсами валют банков. """
    def get_banks_for_exchange(self, currency, exchange_rate):
        """ Метод возвращает список банков с максимальной ценой покупки и минимальной ценой продажи по заданной валюте"""
        all_values = {}
        bank = {}

        for info in exchange_rate:
            for cur_op_name, val in exchange_rate[info].items():
                if cur_op_name in all_values.keys():
                    all_values[cur_op_name].append(val)
                    bank[val] = info
                else:
                    all_values[cur_op_name] = [val]
                    bank[val] = info

        best_values = get_best_values(all_values)
        return get_best_banks(best_values, bank)

    """Метод возвращает лучшую цену исходя из переданного курса по банкам"""
    def get_best_values(self, currency, exchange_rates):
        best_values = {}
        get_all_values(currency, exchange_rates)

        for info, rates in exchange_rates.items():
            if cur_op_name in all_values.keys():
                all_values[cur_op_name].append(val)
                bank[val] = info
            else:
                all_values[cur_op_name] = [val]
                bank[val] = info

        best_values[cur_op] = max(value_list) if (cur_op[4:] == 'buy') else min(value_list)

        return best_values
    """exchange_rates = {'bank_id': {'currency_operation': u'value',}} """
    def get_all_values(self, currency, operation, exchange_rates):
        return [val[currency+'_'+operation] for val in exchange_rates.values() if currency+'_'+operation in val.keys()]

    def

    def get_best_value(self, currency, operation, values):
        return max(values) if operation == 'buy' else min(values)

    def get_bank_by_value(self, value):


        banks = {'Not at this time' : 'see ya...'}

        if (best_values['usd_buy'] > best_values['usd_sell']):
            banks['USD GO GO GO !!!'] = {'from': bank[best_values['usd_buy']], 'to': bank[best_values['usd_sell']]}

        if (best_values['eur_buy'] > best_values['eur_sell']):
            banks['EUR GO GO GO !!!'] = {'from': bank[best_values['eur_buy']], 'to': bank[best_values['eur_sell']]}

        return banks

if __name__ == '__main__':
    pass