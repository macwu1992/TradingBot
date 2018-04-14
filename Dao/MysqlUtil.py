#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:MysqlHandler
AUTHOR:Tong
Create Date:2018/4/14
'''
import pymysql

class Mysql:

    def __init__(self, **kwargs):
        # 打开数据库连接
        self.db = pymysql.connect(host=kwargs['host'], user=kwargs['user'], password=kwargs['password'], database=kwargs['database'], port=int(kwargs['port']), charset='utf8')
        self.cursor = self.db.cursor()

    # SQL 插入语句
    def insert(self, insert_sql, value):

        try:
            # 执行sql语句
            self.cursor.execute(insert_sql, value)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            print("插入未成功：")
            self.db.rollback()
        finally:
            self.db.close()