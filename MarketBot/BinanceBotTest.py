#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:BinanceBotTest
AUTHOR:Tong
Create Date:2018/4/13
'''
import json
from MarketBot.Bots.BinanceBot import *

# 从key文件读取key值

binance_keys = json.loads(open('../MarketAPIs/keys/binance.key','r').read())

binanceBot = BinanceBot(binance_keys["ACCESS_KEY"], binance_keys["SECRET_KEY"])

tickers = binanceBot.get_all_tickers()
print(binanceBot.get_symbol_info('ETHBTC'))