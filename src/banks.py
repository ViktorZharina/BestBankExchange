#!/usr/bin/python
# -*- coding: utf-8 -*-

settings = {
    'currencys'     : ['usd', 'eur'],
    'operations'    : ['buy', 'sell'],
    'usd_buy'       : u'USD покупка',
    'usd_sell'      : u'USD продажа',
    'eur_buy'       : u'EUR покупка',
    'eur_sell'      : u'EUR продажа',
    'memchache_link': u'127.0.0.1:11211'
}

url_bank_info = {
    'http://www.nskbl.ru'                                           : u'Левобережный. Совпаршкольный 13. 900-410. 09.00-20.00',
    'http://novosibirs.pkb.ru/work/informer/currency.asp?87971'     : u'Петрокомерц. Трифонова,22 51-27-60. 10.00-17.00',
    'http://www.rshb.ru/filiali/55/currency-rates.php'              : u'Россельхоз. МосковТракт,д.8б 20-22-24. 09.00-19.30',
    'http://www.skbbank.ru'                                         : u'СКБ Томск, пр. Ленина,94. 51-18-49. 09.00-20.00',
    'http://tomsk.rostbank.ru/offices'                              : u'РОСТ_БАНК ул.Дзержинского,54а. 70-50-51. 09:30 - 19:00',
    'http://www.bank-kansky.ru'                                     : u'Канский пр. Кирова, 35 55-50-90',
    'https://direct.binbank.ru/api/rate.php?city=Томск&callback=?'  : u'БинБанк Кирова,3Б 56-40-37'
}

parse_params = [
    {
        'url'                   :'http://www.nskbl.ru',
        'usd_ankor'				: u'<td>Доллар США</td>',
        'usd_buy_offset'        : 157,
        'usd_sell_offset'       : 274,
        'eur_ankor'				: u'<td>Евро</td>',
        'eur_buy_offset'        : 151,
        'eur_sell_offset'       : 268,
        'offset' 				: 5,
        'encoding'				: 'cp1251'
    },
    {
        'url'                   :'http://novosibirs.pkb.ru/work/informer/currency.asp?87971',
        'usd_ankor'				: u'USD',
        'usd_buy_offset'        : 44,
        'usd_sell_offset'       : 92,
        'eur_ankor'				: u'EUR',
        'eur_buy_offset'        : 44,
        'eur_sell_offset'       : 92,
        'offset' 				: 5,
        'encoding'				: 'cp1251'
    },
    {
        'url'                   : 'http://www.rshb.ru/filiali/55/currency-rates.php',
        'usd_ankor'				: u'Доллар США',
        'usd_buy_offset'        : 24,
        'usd_sell_offset'       : 43,
        'eur_ankor'				: u'ЕВРО',
        'eur_buy_offset'        : 18,
        'eur_sell_offset'       : 37,
        'offset' 				: 5,
        'encoding'				: 'cp1251'
    },
    {
        'url'                   : 'http://www.skbbank.ru',
        'usd_ankor'				: u'td',
        'usd_buy_offset'        : 'val_0',
        'usd_sell_offset'       : 'val_1',
        'eur_ankor'             : u'td',
        'eur_buy_offset'        : 'val_3',
        'eur_sell_offset'       : 'val_4',
        'offset' 				: 5,
        'encoding'				: 'utf-8',
        'method'                : 'soup'
    },
    {
        'url'                   : 'http://tomsk.rostbank.ru/offices',
        'usd_ankor'				: u'USD',
        'usd_buy_offset'        : 12,
        'usd_sell_offset'       : 26,
        'eur_ankor'             : u'EUR',
        'eur_buy_offset'        : 12,
        'eur_sell_offset'       : 26,
        'offset' 				: 5,
        'encoding'				: 'utf-8'
    },
    {
        'url'                   : 'http://www.bank-kansky.ru',
        'name'					: u'Канский',
        'address'				: u'пр. Кирова, 35',
        'phone'					: '55-50-90',
        'work_time'				: '10.00 - 19.00',
        'usd_ankor'				: u'USD',
        'usd_buy_offset'        : 39,
        'usd_sell_offset'       : 71,
        'eur_ankor'				: u'EUR',
        'eur_buy_offset'        : 39,
        'eur_sell_offset'       : 71,
        'offset' 				: 5,
        'encoding'				: 'utf-8'
    },
    {
        'url'                   : 'https://direct.binbank.ru/api/rate.php?city=Томск&callback=?',
        'name'					: u'БинБанк',
        'address'				: u'Кирова,3Б',
        'phone'					: '56-40-37 \t',
        'work_time'				: '9:00-20:00',
        'usd_ankor'				: u'today',
        'eur_ankor'				: u'today',
        'encoding'				: 'utf-8',
        'method'                : 'json'
    }
]
