#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:Rest_Service
NAME:market_handler
AUTHOR:Tong
Create Date:2018/5/6
'''

from abc import abstractmethod, ABCMeta
import Rest_Service.external_API.Huobi.HuobiServices as huobi_service
import Rest_Service.external_API.Binance.binance.client as binance_client

class BaseHandler(metaclass=ABCMeta):

    def  __init__(self):
        pass

    @abstractmethod
    def get_account(self):
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

# #
# init huobi client
# #
class HuobiClient(BaseHandler):
    
    def __init__(self, key):
        huobi_service.set_key(key)
        self.client = huobi_service

    def get_account(self, acct_id=None):
        return self.client.get_balance()

    def get_accounts(self):
        return self.client.get_accounts()

    def get_symbol_info(self, symbol):
        return self.client.get_detail(symbol)

    def get_ticker(self, symbol):
        return self.client.get_ticker(symbol)

    def get_all_tickers(self):
        pass

    def send_order(self, **kwargs):
        return self.client.send_order(**kwargs)

# #
# init huobi client
# #

class BinanceClient(BaseHandler):

    def __init__(self, key):
        self.client = binance_client.Client(key['ACCESS_KEY'], key['SECRET_KEY'])

    def get_account(self):
        return self.client.get_account()

    def get_symbol_info(self, symbol):
        return self.client.get_symbol_info(symbol)

    def get_ticker(self, symbol):
        return self.client.get_ticker(symbol=symbol)

    def get_all_tickers(self):
        self.client.get_all_tickers()

    def send_order(self, **kwargs):
        self.client.create_order(**kwargs)