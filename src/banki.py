#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author Viktor Zharina <viktorz1986@gmail.com>
# CC-BY-SA License

import urllib2
from banks import *
import json
from bs4 import BeautifulSoup
import MySQLdb
import memcache
from decimal import *

getcontext().prec = 4
# Описание работы скрипта
#1.получить обменный курс
#   1.1 получить исходный код страницы
#   1.2 распарсить из страницы значения курсов валют
#   1.3 вернуть значения в виде {'информация_по_банку': {'валюта_операция': значение}}
#
#2 получить и отобразить таблицу курсов из банков
#   2.1 на основании данных п.1 отобразить таблицу в причесанном виде
#3 отобразить информацию по банкам, где покупка больше, чем продажа
#   3.1 на основании обменного курса из п.1 сформировать словарь всех значений
#       по всем валютам_операциям
#   3.2 на основании обменного курса из п.1 поставить в соответствие цену к информации_по_банку
#   3.3 получить лучие цены среди всех банков( макс цена покупки и минимальная цена продажи)
#   3.4 получить информацию_по_банку по лучшей цене


def main():
    bank_rate = get_exchange_rate(parse_params, settings)
    #add_to_mysql(bank_rate)
    add_to_memcache(bank_rate)
    #print (get_currency_table(bank_rate))

def add_to_memcache(bank_rate):
    mc = memcache.Client(['127.0.0.1:11211'], debug=1)
    mc.set('syn', 1)

    for bank_url, exchange_rate in bank_rate.items():
        mc.set(bank_url.encode('utf-8'), exchange_rate)


    mc.set('syn', 0)

    mc.get('http://www.nskbl.ru')
    return 1

def add_to_mysql(bank_rate):
    db = MySQLdb.connect(host="localhost", user="root", passwd="ghtdtl", db="banks", charset='utf8')
    cursor = db.cursor()

    for bank_info, cur_op in bank_rate.items():
        sql = """INSERT INTO exchange_rate (bank_info, usd_buy, usd_sell, eur_buy, eur_sell)
        VALUES ('%(bank_info)s', %(usd_buy)f, %(usd_sell)f, %(eur_buy)f, %(eur_sell)f) """ % {
            "bank_info" : bank_info,
            "usd_buy"   : Decimal(cur_op['usd_buy']),
            "usd_sell"  : Decimal(cur_op['usd_sell']),
            "eur_buy"   : Decimal(cur_op['eur_buy']),
            "eur_sell"  : Decimal(cur_op['eur_sell']),
        }
        cursor.execute(sql)

    db.commit()

    return True

def get_exchange_rate(parse_params, settings):
    bank_rate = {}

    for bank in parse_params:
        source = get_source(bank['url'], bank['encoding'])
        exchange_rate = {}
        for c in settings['currencys']:
            for op in settings['operations']:
                exchange_rate[c +"_" + op] = get_currency_value(c, op, source, bank)
                bank_rate[url_bank_info[bank['url']]] = exchange_rate

    return bank_rate

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

def get_banks_for_exchange(bank_rate):
    all_values = {}
    bank = {}

    for info in bank_rate:
        for cur_op_name, val in bank_rate[info].items():
            if cur_op_name in all_values.keys():
                all_values[cur_op_name].append(val)
                bank[val] = info
            else:
                all_values[cur_op_name] = [val]
                bank[val] = info

    best_values = get_best_values(all_values)
    return get_banks_by_best_values(best_values, bank)

def get_source(url, encoding):
    try:
        fileHandle = urllib2.urlopen(url)
        source = fileHandle.read()
        fileHandle.close()
    except IOError:
        print ('Cannot open URL %s for reading' % url)
        source = u'err'
    return source.decode(encoding, 'ignore')

def get_currency_value(cur, ttype, src, params):
    if ('method' in params.keys()):
        if (params['method'] == 'soup'):
            #process_soup
            soup = BeautifulSoup(src)
            currency_value = soup.find(params[cur + '_ankor'], {'id':params[cur + '_' + ttype + '_offset']}).get_text(strip=True)
        elif (params['method'] == 'json'):
            #process_json
            json_data = json.loads(src)

            if (ttype == 'sell'):
                ##SALE!!!
                currency_value = json_data['today']['sale'][cur]
            else:
                currency_value = json_data['today'][ttype][cur]
            currency_value = str(currency_value)
    else:
        #process_by_hand
        cur_type_offset = params[cur + '_' + ttype + '_offset']
        ankor_idx = src.find(params[cur + '_ankor'])
        buy_start = ankor_idx + cur_type_offset
        currency_value = src[buy_start : buy_start + params['offset']]

    return currency_value.replace(',', '.')

def get_best_values(all_values):
    best_values = {}

    for cur_op, value_list in all_values.items():
        best_values[cur_op] = max(value_list) if (cur_op[4:] == 'buy') else min(value_list)

    return best_values

def get_banks_by_best_values(best_values, bank):

    banks = {'Not at this time' : 'see ya...'}

    if (best_values['usd_buy'] > best_values['usd_sell']):
        banks['USD GO GO GO !!!'] = {'from': bank[best_values['usd_buy']], 'to': bank[best_values['usd_sell']]}

    if (best_values['eur_buy'] > best_values['eur_sell']):
        banks['EUR GO GO GO !!!'] = {'from': bank[best_values['eur_buy']], 'to': bank[best_values['eur_sell']]}

    return banks

if __name__ == "__main__":
    main()


