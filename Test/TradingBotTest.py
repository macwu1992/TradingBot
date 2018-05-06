#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:TradingBotTest
AUTHOR:Tong
Create Date:2018/4/14
'''
import sys
sys.path.append('/root/workspace/TradingBot')
sys.path.append('/root/workspace/TradingBot/Dao')
sys.path.append('/root/workspace/TradingBot/Service')
sys.path.append('/root/workspace/TradingBot/Service/keys')
sys.path.append('/root/workspace/TradingBot/Service/MarketAPIs')
sys.path.append('/root/workspace/TradingBot/Service/MarketAPIs/Huobi')
sys.path.append('/root/workspace/TradingBot/Service/MarketAPIs/Binance')
sys.path.append('/root/workspace/TradingBot/Service/MarketAPIs/Binance/binance')

from Service.TradingBot.PortersBot import *
import time

portersBot = PortersBot(
    binance_keys=json.loads(open('../Service/keys/binance.key','r').read()),
    huobi_keys=json.loads(open('../Service/keys/huobi.key','r').read())
)

# while 1:
#     portersBot.perform()
#     time.sleep(10)

# 币安下单最小数目为0.001个btc
while 1:
    portersBot.porting(diff_floor=3, amount=0.0015)
    time.sleep(10)