#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import banks
import json
from bs4 import BeautifulSoup

def main():
    print "Банк \t\t\t\t\t USDBuy\t\tUSDSell\t\tEURBuy\t\tEURSell"

    currency_list = ['usd', 'eur']
    type_list = ['buy', 'sell']

    all_prices = {
        'usd':
        {
            'buy': { 'prices': [] },
            'sell': { 'prices': [] }
        },
        'eur':
        {
            'buy': { 'prices': [] },
            'sell': { 'prices': [] }
        }
    }

    best_bank_price = {}

    for url in banks.params.keys():
        print url
        params = banks.params[url]
        src = getSource(url, params['encoding'])
        header = params['name'] + ' ' +  params['address'] + ' ' + params['phone'] + ' '
        body = ""

        for c in currency_list:
            for t in type_list:
                price = getPrice(c, t, src, params)
                all_prices[c][t]['prices'].append(price)
                best_bank_price[price] = header
                body += '\t|' + price + '\t|'

        print (header + body).encode('utf-8')
        print '==============================================================================================================='

    best_buy_price = getBest('usd', 'buy', all_prices).replace(',', '.')
    best_sell_price = getBest('usd', 'sell', all_prices).replace(',', '.')

    print best_buy_price, best_sell_price

    if (best_buy_price > best_sell_price):
        print "RUR na USD " + best_buy_price.encode('utf-8') + " v " + best_bank_price[best_buy_price].encode('utf-8') + " USD na RUR " + best_sell_price.encode('utf-8') + " v " + best_bank_price[best_sell_price].encode('utf-8')

    best_buy_price = getBest('eur', 'buy', all_prices)
    best_sell_price = getBest('eur', 'sell', all_prices)

    print best_buy_price, best_sell_price

    if (best_buy_price > best_sell_price):
        print "RUR na EUR v " + best_bank_price[best_buy_price].encode('utf-8') + " EUR na RUR v " + best_bank_price[best_sell_price].encode('utf-8')

def getSource(url, encoding):
    try:
        fileHandle = urllib2.urlopen(url)
        source = fileHandle.read()
        fileHandle.close()
    except IOError:
        print ('Cannot open URL %s for reading' % url)
        source = u'err'
    return source.decode(encoding, 'ignore')

def getBest(cur, ttype, all_prices):
    if (ttype == 'buy'):
        return max(all_prices[cur][ttype]['prices'])
    elif (ttype == 'sell'):
        return min(all_prices[cur][ttype]['prices'])
    else:
        return 0

def getPrice(cur, ttype, src, params):
    if ('method' in params.keys()):
        if (params['method'] == 'soup'):
            soup = BeautifulSoup(src)
            price = soup.find(params[cur + '_ankor'], {'id':params[cur + '_' + ttype + '_offset']}).get_text(strip=True)
        elif (params['method'] == 'json'):
            json_data = json.loads(src)
            if (ttype == 'sell'):
                price = json_data['today']['sale'][cur]
            else:
                price = json_data['today'][ttype][cur]
    else:
        cur_type_offset = params[cur + '_' + ttype + '_offset']
        ankor_idx = src.find(params[cur + '_ankor'])
        buy_start = ankor_idx + cur_type_offset
        price = src[buy_start : buy_start + params['offset']]
    return price.replace(',', '.')

if __name__ == "__main__":
    main()


