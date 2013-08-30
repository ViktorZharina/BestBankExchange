#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from banks import *
import json
from bs4 import BeautifulSoup

def main():
    bank_rate = {}

    for bank in banks_info:
        source = get_source(bank['url'], bank['encoding'])
        info = (bank['name'] + ' ' + bank['address'] + ' ' + bank['phone'] + ' ')
        bank_rate[info] = get_exchange_rate(source, bank, settings)

    table = get_currency_table(bank_rate)
    print (table)
    banks = get_banks_for_exchange(bank_rate)
    print banks

def get_source(url, encoding):
    try:
        fileHandle = urllib2.urlopen(url)
        source = fileHandle.read()
        fileHandle.close()
    except IOError:
        print ('Cannot open URL %s for reading' % url)
        source = u'err'
    return source.decode(encoding, 'ignore')

def get_currency_table(bank_rate):
    s = ""
    table = ""
    for info in bank_rate.keys():
        for k,v in bank_rate[info].items():
            s += "\t " + k + " " + v + " | "
        table += info + s + '\n' + 150 * "=" + '\n'
        info = ""
        s = ""

    return table.encode('utf-8')

def get_exchange_rate(src, bank_params, settings):
    exchange_rate = {}
    for c in settings['currencys']:
        for op in settings['operations']:
            exchange_rate[c +"_" + op] = get_currency_value(c, op, src, bank_params)
    return exchange_rate

def get_currency_value(cur, ttype, src, params):
    if ('method' in params.keys()):
        if (params['method'] == 'soup'):
            soup = BeautifulSoup(src)
            currency_value = soup.find(params[cur + '_ankor'], {'id':params[cur + '_' + ttype + '_offset']}).get_text(strip=True)
        elif (params['method'] == 'json'):
            json_data = json.loads(src)

            if (ttype == 'sell'):
                ##SALE!!!
                currency_value = json_data['today']['sale'][cur]
            else:
                currency_value = json_data['today'][ttype][cur]
            currency_value = str(currency_value)
    else:
        cur_type_offset = params[cur + '_' + ttype + '_offset']
        ankor_idx = src.find(params[cur + '_ankor'])
        buy_start = ankor_idx + cur_type_offset
        currency_value = src[buy_start : buy_start + params['offset']]

    return currency_value.replace(',', '.')

def get_banks_for_exchange(bank_rate):
    all_values = {}
    bank = {}

    #get_all_curency_values

    for info in bank_rate:
        for cur_op_name, val in bank_rate[info].items():
            if cur_op_name in all_values.keys():
                all_values[cur_op_name].append(val)
                bank[val] = info
            else:
                all_values[cur_op_name] = [val]
                bank[val] = info

    best_values = get_best_values(all_values)
    best_banks = get_banks_by_best_values(best_values, bank)
    print best_banks
    return best_banks

def get_best_values(all_values):
    best_values = {}

    for cur_op, value_list in all_values.items():
        best_values[cur_op] = max(value_list) if (cur_op[4:] == 'buy') else min(value_list)

    return best_values

def must_exchange(best_banks):
    best_banks

def get_banks_by_best_values(best_values, bank):

    banks = {'Not at this time' : 'see ya...'}

    if (best_values['usd_buy'] > best_values['usd_sell']):
        banks['USD GO GO GO !!!'] = {'from': bank[best_values['usd_buy']], 'to': bank[best_values['usd_sell']]}

    if (best_values['eur_buy'] > best_values['eur_sell']):
        banks['EUR GO GO GO !!!'] = {'from': bank[best_values['eur_buy']], 'to': bank[best_values['eur_sell']]}

    return banks

if __name__ == "__main__":
    main()


