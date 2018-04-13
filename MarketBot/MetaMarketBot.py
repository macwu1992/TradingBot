#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta

'''
定义市场接口
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