#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:HuobiBot
AUTHOR:Tong
Create Date:2018/4/13
'''
from MarketBot.MetaMarketBot import *
from Utils import key
import HuobiServices as service
import json

class HuobiBot(IMarketBot):
    def __init__(self, ACCESS_KEY, SECRET_KEY):
        key.ACCESS_KEY = ACCESS_KEY
        key.SECRET_KEY = SECRET_KEY

    def get_Account(self):
        return service.get_accounts()

    """
        :param symbol
        :return:虚拟币的价格
    """
    def get_symbol_info(self, symbol):
        return service.get_detail(symbol)

    def get_ticker(self, symbol):
        return service.get_ticker(symbol)

    def get_all_tickers(self):
        symbols = service.get_symbols()

        if symbols['status'] == 'ok':
            #get tickers
            tickers = [
                {
                    'symbol':x['base-currency']+x['quote-currency'],
                    'price':service.get_ticker(x['base-currency']+x['quote-currency'])
                }
                for x in symbols['data']
            ]
            return tickers
        else:
            return

    """
            :param amount: 
            :param source: 如果使用借贷资产交易，请在下单接口,请求参数source中填写'margin-api'
            :param symbol: 
            :param _type: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
            :param price: 
            :return: 
        """
    def send_order(self, symbol, amount, _type):
        return service.send_order(amount=amount, symbol=symbol, _type=_type)
