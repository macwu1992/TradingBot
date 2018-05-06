#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:Rest_Service
NAME:test
AUTHOR:Tong
Create Date:2018/5/6
'''

import json

from Rest_Service.market_handler import HuobiClient
from Rest_Service.market_handler import BinanceClient

huobi_keys = json.loads(open('./keys/huobi.key','r').read())
binance_keys = json.loads(open('./keys/binance.key','r').read())

huobi_client = HuobiClient(huobi_keys)
binance_client = BinanceClient(binance_keys)

print(huobi_client.get_account(acct_id=874234))
print(binance_client.get_account())