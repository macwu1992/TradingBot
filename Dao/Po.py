#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:Po
AUTHOR:Tong
Create Date:2018/4/14
'''
class diff_btcusdt_binance_huobi_po:
    def __init__(self):
        self.id = 0
        self.symbol = ''
        self.ask_price1 = 0
        self.bid_price1 = 0
        self.ask_price2 = 0
        self.bid_price2 = 0

    def model2po(self, model):
        self.symbol     = model['symbol']
        self.ask_price1 = model['ask1']
        self.bid_price1 = model['bid1']
        self.ask_price2 = model['ask2']
        self.bid_price2 = model['bid2']
