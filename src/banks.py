#!/usr/bin/python
# -*- coding: utf-8 -*-
params = {
'http://www.nskbl.ru':
{
	'name'					: u'Левобережный',
	'address'				: u'Совпаршкольный 13',
	'phone'					: '900-410',
	'work_time'				: '09.00-20.00',
	'usd_ankor'				: u'<td>Доллар США</td>',
	'usd_buy_offset'                        : 157,
	'usd_sell_offset'                       : 274,
	'eur_ankor'				: u'<td>Евро</td>',
	'eur_buy_offset'                        : 151,
	'eur_sell_offset'                       : 268,
	'offset' 				: 5,
	'encoding'				: 'cp1251'
},
'http://novosibirs.pkb.ru/work/informer/currency.asp?87971':
{
	'name'					: u'Петрокомерц',
	'address'				: u'Трифонова,22',
	'phone'					: '51-27-60',
	'work_time'				: '10.00 - 17.00',
	'usd_ankor'				: u'USD',
	'usd_buy_offset'                        : 44,
	'usd_sell_offset'                       : 92,
	'eur_ankor'				: u'EUR',
	'eur_buy_offset'                        : 44,
	'eur_sell_offset'                       : 92,
	'offset' 				: 5,
	'encoding'				: 'cp1251'
},
 'http://www.rshb.ru/filiali/55/currency-rates.php':
 {
 	'name'					: u'Россельхоз',
 	'address'				: u'МосковТракт,д.8б',
 	'phone'					: '20-22-24',
 	'work_time'				: '09.00-19.30',
 	'usd_ankor'				: u'Доллар США',
 	'usd_buy_offset'                        : 24,
 	'usd_sell_offset'                       : 43,
 	'eur_ankor'				: u'ЕВРО',
 	'eur_buy_offset'                        : 18,
 	'eur_sell_offset'                       : 37,
 	'offset' 				: 5,
 	'encoding'				: 'cp1251'
 },
'http://www.skbbank.ru':
{
	'name'					: u'СКБ',
	'address'				: u'Томск, пр. Ленина,94',
	'phone'					: '51-18-49',
	'work_time'				: '09.00-20.00',
	'usd_ankor'				: u'td',
        'usd_buy_offset'                        : 'val_0',
        'usd_sell_offset'                       : 'val_1',
	'eur_ankor'                         	: u'td',
        'eur_buy_offset'                        : 'val_3',
	'eur_sell_offset'                       : 'val_4',
	'offset' 				: 5,
	'encoding'				: 'utf-8',
        'method'                                : 'soup'
},
    'http://tomsk.rostbank.ru/offices':
    {
	'name'					: u'РОСТ_БАНК',
	'address'				: u'ул.Дзержинского,54а',
	'phone'					: '70-50-51',
	'work_time'				: '09:30 - 19:00',
	'usd_ankor'				: u'USD',
	'usd_buy_offset'                        : 12,
	'usd_sell_offset'                       : 26,
	'eur_ankor'                         	: u'EUR',
	'eur_buy_offset'                        : 12,
	'eur_sell_offset'                       : 26,
	'offset' 				: 5,
	'encoding'				: 'utf-8'
},
'http://www.bank-kansky.ru':
{
	'name'					: u'Канский',
	'address'				: u'пр. Кирова, 35',
	'phone'					: '55-50-90',
	'work_time'				: '10.00 - 19.00',
	'usd_ankor'				: u'USD',
	'usd_buy_offset'                        : 39,
	'usd_sell_offset'                       : 71,
	'eur_ankor'				: u'EUR',
	'eur_buy_offset'                        : 39,
	'eur_sell_offset'                       : 71,
	'offset' 				: 5,
	'encoding'				: 'utf-8'
},
'https://direct.binbank.ru/api/rate.php?city=Томск&callback=?':
    {
	'name'					: u'БинБанк',
	'address'				: u'Кирова,3Б',
	'phone'					: '56-40-37',
	'work_time'				: '9:00-20:00',
	'usd_ankor'				: u'today',
	'eur_ankor'				: u'today',
	'encoding'				: 'utf-8',
        'method'                                : 'json'
	}

}
