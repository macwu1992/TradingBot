#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:BotTest
AUTHOR:Tong
Create Date:2018/4/13
'''

from MarketBot.Bots.HuobiBot import *
import json

# 从key文件读取key值

huobi_keys = json.loads(open('../MarketAPIs/keys/huobi.key','r').read())

huobiBot = HuobiBot(huobi_keys["ACCESS_KEY"], huobi_keys["SECRET_KEY"])

# tickers = huobiBot.get_all_tickers()
# print(huobiBot.get_symbol_info('eosbtc'))
print(huobiBot.get_ticker('ethusdt'))