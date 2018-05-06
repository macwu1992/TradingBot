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

    def model2po(self, **kwargs):
        self.symbol     = kwargs['symbol']
        self.ask_price1 = kwargs['ask1']
        self.bid_price1 = kwargs['bid1']
        self.ask_price2 = kwargs['ask2']
        self.bid_price2 = kwargs['bid2']

class porting_flow_po:
    def __init__(self):
        self.id                 = 0
        self.symbol             = ''
        self.tradingIdMarket1   = 0
        self.tradingIdMarket2   = 0
        self.isMarket1Success   = 0
        self.isMarket2Success   = 0
        self.amountMarket1      = 0
        self.amountMarket2      = 0
        self.priceMarket1       = 0
        self.priceMarket2       = 0

    def model2po(self, model):
        self.id               = model['id']
        self.symbol           = model['symbol']
        self.tradingIdMarket1 = model['tradingIdMarket1']
        self.tradingIdMarket2 = model['tradingIdMarket2']
        self.isMarket1Success = model['isMarket1Success']
        self.isMarket2Success = model['isMarket2Success']
        self.amountMarket1    = model['amountMarket1']
        self.amountMarket2    = model['amountMarket2']
        self.priceMarket1     = model['priceMarket1']
        self.priceMarket2     = model['priceMarket2']