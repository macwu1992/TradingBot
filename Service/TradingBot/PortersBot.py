#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:PortersBot
AUTHOR:Tong
Create Date:2018/4/13
'''
from Service.MarketBot.MarketBot import *
from Dao.DaoClass import diff_btcusdt_binance_huobi_dao as diff_dao
from Dao.Po import diff_btcusdt_binance_huobi_po as diff_po

from Dao.DaoClass import porting_flow_dao as porting_dao
from Dao.Po import porting_flow_po as porting_po

class PortersBot:

    def __init__(self, **kwargs):
        self.dao = diff_dao()
        self.binance_keys = kwargs['binance_keys']

        self.binanceBot = BinanceBot(self.binance_keys["ACCESS_KEY"], self.binance_keys["SECRET_KEY"])
        self.huobi_keys = kwargs['huobi_keys']

        self.huobiBot = HuobiBot(self.huobi_keys["ACCESS_KEY"], self.huobi_keys["SECRET_KEY"])

    def diff_by_symbol(self, symbol, market1=None, market2=None):
        ''' get ticker by symbol'''
        try:
            binance_ticker = self.binanceBot.get_ticker(symbol)
            binance_bid_price = binance_ticker['bidPrice']
            binance_ask_price = binance_ticker['askPrice']

            huobi_ticker = self.huobiBot.get_ticker(symbol)
            huobi_bid_price = str(huobi_ticker['tick']['bid'][0])
            huobi_ask_price = str(huobi_ticker['tick']['ask'][0])

            return {
                'symbol': symbol,
                'ask1': binance_ask_price,
                'bid1': binance_bid_price,
                'ask2': huobi_ask_price,
                'bid2': huobi_bid_price,
            }

        except BinanceAPIException as err:
            print(err.__str__())
        except HuobiSymbolFoundException as err:
            print(err.__str__())

    def get_price_diff(self):
        return self.diff_by_symbol('BTCUSDT')

    def porting(self, diff_floor, amount, threshold):
        diff_btc_usdt = self.get_price_diff()

        tex_binance = 0.001
        tax_huobi = 0.002
        # max_diff = max(diff_btc_usdt['bid1'] - diff_btc_usdt['ask2'], diff_btc_usdt['bid2'] - diff_btc_usdt['ask1'])

        # binance_order_list = self.binanceBot.order_list(symbol='LRCETH')
        # huobi_order_list1 = self.huobiBot.order_list(symbol='OMGUSDT')
        # huobi_order_list2 = self.huobiBot.orders_matchresults(symbol='OMGUSDT')

        # print(binance_order_list)
        # print(huobi_order_list1)
        # print(huobi_order_list2)

        if float(diff_btc_usdt['bid1']) - float(diff_btc_usdt['ask2']) > diff_floor:
            # sell-order
            market1_order_reponse = self.binanceBot.send_order(symbol='BTCUSDT', side='SELL', type='LIMIT',
                                                             quantity=amount, price=diff_btc_usdt['bid1'])

            tranding_id_market1 = market1_order_reponse['orderId']

            # buy-order
            market2_order_reponse = self.huobiBot.send_order(symbol='BTCUSDT', amount=amount, _type='buy-limit', price=diff_btc_usdt['ask2'])

            tranding_id_market2 = market2_order_reponse['account-id']

            # insert into porting_flow
            dao = diff_dao()
            po = diff_po()
            po.model2po(
                symbol          ='BTCUSDT' ,
                tradingIdMarket1=tranding_id_market1,
                tradingIdMarket2=tranding_id_market2,
                isMarket1Success=0,
                isMarket2Success=0,
                amountMarket1   =amount,
                amountMarket2   =amount,
                priceMarket1    =diff_btc_usdt['bid1'],
                priceMarket2    =diff_btc_usdt['ask2']
            )

            dao.insert(po)

            # 轮询tranding_id_market1,tranding_id_market2是否成功
            market1_order_info = self.binanceBot.order_info(symbol='BTCUSDT', order_id=tranding_id_market1)
            market2_order_info = self.huobiBot.order_info(order_id=tranding_id_market2)



    def perform(self):
        diff_btc_usdt = self.get_price_diff()
        po = diff_po()
        po.model2po(diff_btc_usdt)
        self.dao.insert(po)

    # get tickers
    # lines = open('./symbols').read().split('\n')

    # def trans_huobi_tick(l):
    #     ticker = huobiBot.get_ticker(l)
    #     if ticker and ticker['status'] == 'ok':
    #         ticker = {'symbol': l.upper(), 'price': ticker['tick']['ask'][0]}
    #         return ticker
    #     else:
    #         return

    # huobi_tickers = [trans_huobi_tick(l) for l in lines]
    # huobi_tickers.remove(None)

    # 两个交易所相同的币种
    # union_symbol = list(set([ticker['symbol'].upper() for ticker in huobi_tickers]).intersection(set([ticker['symbol'].upper() for ticker in binance_ticker_list])))

    # 计算差价
    # diff = [{'symbol': u_s, 'price_diff': float(h_t['price']) - float(b_t['price'])} for u_s in union_symbol for h_t in huobi_tickers for b_t in binance_ticker_list if h_t['symbol'] == u_s and b_t['symbol'] == u_s]

    # 统计差价最大的币种
    # diff.sort(key=lambda x:(x['price_diff'],x['symbol']), reverse=True)