#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:PortersBot
AUTHOR:Tong
Create Date:2018/7/25
'''

class PortersBot:

    def __init__(self, **kwargs):
        # init two market client
        self.key1 = kwargs.get('key1')
        self.key2 = kwargs.get('key2')

    def port(self, **kwargs):
        sale_price = kwargs.get('sale_price')
        buy_price = kwargs.get('buy_price')

        amount = kwargs.get('amount')