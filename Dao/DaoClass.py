#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:Dao
AUTHOR:Tong
Create Date:2018/4/14
'''
from Dao import *
from Dao.MysqlUtil import Mysql
import time

class diff_btcusdt_binance_huobi_dao():
    def __init__(self):
        self.table_name = 'diff_btcusdt_binance_huobi'
        self.mysql = Mysql(host='192.168.1.101', user='root', password='123456', database='TradingBot', port='3307')

    def insert(self, po):
        #INSERT INTO `STU_MSG` (`ID`, `NAME`, `AGE`) VALUES (NULL, '', NULL),
        insert_sql = '''INSERT INTO diff_btcusdt_binance_huobi VALUES (null, %s,%s,%s,%s,%s,%s)'''
        value = (getattr(po, 'symbol'), getattr(po, 'ask_price1'), getattr(po, 'bid_price1'), getattr(po, 'ask_price1'), getattr(po, 'bid_price2'), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        self.mysql.insert(insert_sql, value)

    def delete(self, po):
        pass

    def update(self, po):
        pass

    def query(self, po):
        pass


