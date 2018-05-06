#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from binance.client import *

from Utils import *
import HuobiServices as service
from HuobiExceptions import *
'''
定义市场机器人接口
'''
class IMarketBot(metaclass=ABCMeta):
    @abstractmethod
    def get_Account(self):
        pass

    @abstractmethod
    def get_symbol_info(self, symbol):
        pass

    @abstractmethod
    def get_ticker(self, symbol):
        pass

    @abstractmethod
    def get_all_tickers(self):
        pass

    @abstractmethod
    def send_order(self, **kwargs):
        pass

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
        return self.client.get_ticker(symbol=symbol.upper())

    def get_all_tickers(self):
        return self.client.get_all_tickers()

    def send_order(self, symbol, side, type, quantity, price, timeInForce='GTC'):
        self.client.create_order(symbol=symbol.upper(), side=side, type=type, quantity=quantity, price=price, timeInForce=timeInForce)

    def order_info(self, symbol, order_id):
        self.client.get_order(symbol=symbol, order_id=order_id)

    def order_list(self, symbol, order_id, timestamp):
        self.client.get_all_orders(symbol=symbol, timestamp=timestamp)

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
        ticker = service.get_ticker(symbol.lower())

        if ticker and ticker['status'] == 'ok':
            return service.get_ticker(symbol.lower())
        else:
            raise HuobiSymbolFoundException

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
    def send_order(self, symbol, amount, _type, price=0):
        return service.send_order(amount=amount, symbol=symbol.lower(), _type=_type, price=price)

    def order_list(self, symbol, states=''):
        return service.orders_list(symbol=symbol.lower(), states=states)

    def order_info(self, order_id):
        return service.order_info(order_id)

    def orders_matchresults(self, symbol):
        return service.orders_matchresults(symbol=symbol.lower())