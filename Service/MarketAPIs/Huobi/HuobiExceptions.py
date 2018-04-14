#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:Exceptions
AUTHOR:Tong
Create Date:2018/4/14
'''

class HuobiSymbolFoundException(Exception):
    def __init__(self):
        self.err_code = '1001'
        self.err_msg = 'Symbol Found'

    def __str__(self):
        return 'HuobiApiException ' + self.err_code + ':' + self.err_msg