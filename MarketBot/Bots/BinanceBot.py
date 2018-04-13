#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:BinanceBot
AUTHOR:Tong
Create Date:2018/4/13
'''

from MarketAPIs.Binance.binance.client import Client
from MarketBot.MetaMarketBot import *

class BinanceBot(IMarketBot):

    def __init__(self, API_KEY, SECRET_KEY):
        API_KEY = API_KEY
        SECRET_KEY = SECRET_KEY

        self.client = Client(API_KEY, SECRET_KEY)

    def get_Account(self):
        return self.client.get_account()

    def get_symbol_info(self, symbol):
        return self.client.get_symbol_info(symbol)

    def get_ticker(self, symbol):
        return self.client.get_ticker(symbol=symbol)

    def get_all_tickers(self):
        return self.client.get_all_tickers()

    def send_order(self, symbol, side, type, quantity, timestamp):
        self.client.create_order(symbol=symbol, side=side, type=type, quantity=quantity, timestamp=timestamp)