#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:TradingBotTest
AUTHOR:Tong
Create Date:2018/4/14
'''
from Service.TradingBot.PortersBot import *
import time

portersBot = PortersBot(
    binance_keys=json.loads(open('../Service/keys/binance.key','r').read()),
    huobi_keys=json.loads(open('../Service/keys/huobi.key','r').read())
)

while 1:
    portersBot.perform()
    time.sleep(1)