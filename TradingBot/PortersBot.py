#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:PortersBot
AUTHOR:Tong
Create Date:2018/4/13
'''
from MarketBot.Bots.BinanceBot import *
from MarketBot.Bots.HuobiBot import *
import operator

binance_keys = json.loads(open('../MarketAPIs/keys/binance.key','r').read())
binanceBot = BinanceBot(binance_keys["ACCESS_KEY"], binance_keys["SECRET_KEY"])

huobi_keys = json.loads(open('../MarketAPIs/keys/huobi.key','r').read())
huobiBot = HuobiBot(huobi_keys["ACCESS_KEY"], huobi_keys["SECRET_KEY"])

# get tickers
lines = open('./symbols').read().split('\n')

def trans_huobi_tick(l):
    ticker = huobiBot.get_ticker(l)
    if ticker and ticker['status'] == 'ok':
        ticker = {'symbol': l.upper(), 'price': ticker['tick']['ask'][0]}
        return ticker
    else:
        return

huobi_tickers = [trans_huobi_tick(l) for l in lines]
huobi_tickers.remove(None)
binance_tickers = binanceBot.get_all_tickers()

# 两个交易所相同的币种
union_symbol = list(set([ticker['symbol'].upper() for ticker in huobi_tickers]).intersection(set([ticker['symbol'].upper() for ticker in binance_tickers])))

# print(t['price'] for t in huobi_tickers if t['symbol'] == 'BTCUSDT')
# print(t['price'] for t in binance_tickers if t['symbol'] == 'BTCUSDT')

# 计算差价
diff = [{'symbol': u_s, 'price_diff': float(h_t['price']) - float(b_t['price'])} for u_s in union_symbol for h_t in huobi_tickers for b_t in binance_tickers if h_t['symbol'] == u_s and b_t['symbol'] == u_s]

# 统计差价最大的币种
diff.sort(key=lambda x:(x['price_diff'],x['symbol']), reverse=True)