#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from Service.Market_API.Utils import *

'''
Market data API
'''
# 获取KLine
def get_kline(symbol, period, size=150):
    """
    :param symbol
    :param period: 可选值：{1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year }
    :param size: 可选值： [1,2000]
    :return:
    """
    params = {'symbol': symbol,
              'period': period,
              'size': size}

    url = MARKET_URL + '/market/history/kline'
    return http_get_request(url, params)


# 获取marketdepth
def get_depth(symbol, type):
    """
    :param symbol
    :param type: 可选值：{ percent10, step0, step1, step2, step3, step4, step5 }
    :return:
    """
    params = {'symbol': symbol,
              'type': type}

    url = MARKET_URL + '/market/depth'
    return http_get_request(url, params)


# 获取tradedetail
def get_trade(symbol):
    """
    :param symbol
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/trade'
    return http_get_request(url, params)


# 获取merge ticker
def get_ticker(symbol):
    """
    :param symbol:
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/detail/merged'
    return http_get_request(url, params)


# 获取 Market Detail 24小时成交量数据
def get_detail(symbol):
    """
    :param symbol
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/detail'
    return http_get_request(url, params)


# 获取  支持的交易对
def get_symbols(long_polling=None):
    """

    """
    params = {}
    if long_polling:
        params['long-polling'] = long_polling
    path = '/v1/common/symbols'
    return api_key_get(params, path)


'''
Trade/Account API
'''


def get_accounts():
    """
    :return:
    """
    path = "/v1/account/accounts"
    params = {}
    return api_key_get(params, path)


ACCOUNT_ID = None


# 获取当前账户资产
def get_balance(acct_id=None):
    """
    :param acct_id
    :return:
    """
    global ACCOUNT_ID

    if not acct_id:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id'];

    url = "/v1/account/accounts/{0}/balance".format(acct_id)
    params = {"account-id": acct_id}
    return api_key_get(params, url)


# 下单

# 创建并执行订单
def send_order(amount, source, symbol, _type, price=0):
    """
    :param amount:
    :param source: 如果使用借贷资产交易，请在下单接口,请求参数source中填写'margin-api'
    :param symbol:
    :param _type: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param price:
    :return:
    """
    try:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id']
    except BaseException as e:
        print ('get acct_id error.%s' % e)
        acct_id = ACCOUNT_ID

    params = {"account-id": acct_id,
              "amount": amount,
              "symbol": symbol,
              "type": _type,
              "source": source}
    if price:
        params["price"] = price

    url = '/v1/order/orders/place'
    return api_key_post(params, url)


# 撤销订单
def cancel_order(order_id):
    """

    :param order_id:
    :return:
    """
    params = {}
    url = "/v1/order/orders/{0}/submitcancel".format(order_id)
    return api_key_post(params, url)


# 查询某个订单
def order_info(order_id):
    """

    :param order_id:
    :return:
    """
    params = {}
    url = "/v1/order/orders/{0}".format(order_id)
    return api_key_get(params, url)


# 查询某个订单的成交明细
def order_matchresults(order_id):
    """

    :param order_id:
    :return:
    """
    params = {}
    url = "/v1/order/orders/{0}/matchresults".format(order_id)
    return api_key_get(params, url)


# 查询当前委托、历史委托
def orders_list(symbol, states, types=None, start_date=None, end_date=None, _from=None, direct=None, size=None):
    """

    :param symbol:
    :param states: 可选值 {pre-submitted 准备提交, submitted 已提交, partial-filled 部分成交, partial-canceled 部分成交撤销, filled 完全成交, canceled 已撤销}
    :param types: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param start_date:
    :param end_date:
    :param _from:
    :param direct: 可选值{prev 向前，next 向后}
    :param size:
    :return:
    """
    params = {'symbol': symbol,
              'states': states}

    if types:
        params[types] = types
    if start_date:
        params['start-date'] = start_date
    if end_date:
        params['end-date'] = end_date
    if _from:
        params['from'] = _from
    if direct:
        params['direct'] = direct
    if size:
        params['size'] = size
    url = '/v1/order/orders'
    return api_key_get(params, url)


# 查询当前成交、历史成交
def orders_matchresults(symbol, types=None, start_date=None, end_date=None, _from=None, direct=None, size=None):
    """

    :param symbol:
    :param types: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param start_date:
    :param end_date:
    :param _from:
    :param direct: 可选值{prev 向前，next 向后}
    :param size:
    :return:
    """
    params = {'symbol': symbol}

    if types:
        params[types] = types
    if start_date:
        params['start-date'] = start_date
    if end_date:
        params['end-date'] = end_date
    if _from:
        params['from'] = _from
    if direct:
        params['direct'] = direct
    if size:
        params['size'] = size
    url = '/v1/order/matchresults'
    return api_key_get(params, url)


# 申请提现虚拟币
def withdraw(address, amount, currency, fee=0, addr_tag=""):
    """

    :param address_id:
    :param amount:
    :param currency:btc, ltc, bcc, eth, etc ...(火币Pro支持的币种)
    :param fee:
    :param addr-tag:
    :return: {
              "status": "ok",
              "data": 700
            }
    """
    params = {'address': address,
              'amount': amount,
              "currency": currency,
              "fee": fee,
              "addr-tag": addr_tag}
    url = '/v1/dw/withdraw/api/create'

    return api_key_post(params, url)


# 申请取消提现虚拟币
def cancel_withdraw(address_id):
    """

    :param address_id:
    :return: {
              "status": "ok",
              "data": 700
            }
    """
    params = {}
    url = '/v1/dw/withdraw-virtual/{0}/cancel'.format(address_id)

    return api_key_post(params, url)


'''
借贷API
'''


# 创建并执行借贷订单


def send_margin_order(amount, source, symbol, _type, price=0):
    """
    :param amount:
    :param source: 'margin-api'
    :param symbol:
    :param _type: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param price:
    :return:
    """
    try:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id']
    except BaseException as e:
        print ('get acct_id error.%s' % e)
        acct_id = ACCOUNT_ID

    params = {"account-id": acct_id,
              "amount": amount,
              "symbol": symbol,
              "type": _type,
              "source": 'margin-api'}
    if price:
        params["price"] = price

    url = '/v1/order/orders/place'
    return api_key_post(params, url)


# 现货账户划入至借贷账户


def exchange_to_margin(symbol, currency, amount):
    """
    :param amount:
    :param currency:
    :param symbol:
    :return:
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}

    url = "/v1/dw/transfer-in/margin"
    return api_key_post(params, url)


# 借贷账户划出至现货账户


def margin_to_exchange(symbol, currency, amount):
    """
    :param amount:
    :param currency:
    :param symbol:
    :return:
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}

    url = "/v1/dw/transfer-out/margin"
    return api_key_post(params, url)


# 申请借贷
def get_margin(symbol, currency, amount):
    """
    :param amount:
    :param currency:
    :param symbol:
    :return:
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}
    url = "/v1/margin/orders"
    return api_key_post(params, url)


# 归还借贷
def repay_margin(order_id, amount):
    """
    :param order_id:
    :param amount:
    :return:
    """
    params = {"order-id": order_id,
              "amount": amount}
    url = "/v1/margin/orders/{0}/repay".format(order_id)
    return api_key_post(params, url)


# 借贷订单
def loan_orders(symbol, currency, start_date="", end_date="", start="", direct="", size=""):
    """
    :param symbol:
    :param currency:
    :param direct: prev 向前，next 向后
    :return:
    """
    params = {"symbol": symbol,
              "currency": currency}
    if start_date:
        params["start-date"] = start_date
    if end_date:
        params["end-date"] = end_date
    if start:
        params["from"] = start
    if direct and direct in ["prev", "next"]:
        params["direct"] = direct
    if size:
        params["size"] = size
    url = "/v1/margin/loan-orders"
    return api_key_get(params, url)


# 借贷账户详情,支持查询单个币种
def margin_balance(symbol):
    """
    :param symbol:
    :return:
    """
    params = {}
    url = "/v1/margin/accounts/balance"
    if symbol:
        params['symbol'] = symbol

    return api_key_get(params, url)


def moving_average(result, begin, end, size):
    sum = 0.0
    num = count = 0
    while count < end:
        if count >= begin:
            sum += result[count]['close']
            num += 1
        count += size
    sum /= num
    return sum


def find_balance(symbol, type):
    balance = get_balance()
    for key in balance['data']['list']:
        if key['currency'] == symbol and key['type'] == type:
            return float(key['balance'])
    return -1.0


def sell(percent, symbol):
    number = round(find_balance('eos', 'trade') - 0.01, 2)
    if number > 0:
        order = send_order(number * percent, 'api', symbol, 'sell-market', 0)
        if order['status'] == 'ok':
            print ('sell success')
            return number * percent
    return -1.0


def buy(percent, symbol):
    money = round(find_balance('usdt', 'trade') - 0.0001, 4)
    if money > 0:
        order = send_order(money * percent, 'api', symbol, 'buy-market', 0)
        if order['status'] == 'ok':
            print('buy success')
            detail = order_matchresults(order['data'])
            return float(detail['data'][0]['price'])
    return -1.0


def check_account():
    usdt = find_balance('usdt', 'trade')
    eos = find_balance('eos', 'trade')
    if usdt < 0.1:
        return 1.0
    elif eos < 0.1:
        return 0.0
    else:
        res = get_kline('eosusdt', '1min', 1)
        if eos > (usdt / float(res['data'][0]['close'])):
            return 0.75
        else:
            return 0.25


def price_difference(price1, price2):
    if price1 * 0.9945 < price2:
        return 1
    return 0


if __name__ == '__main__':
    symbol = 'eosusdt'
    cost_price = 0.0
    while (1):
        res1 = get_kline(symbol, '15min', 10)
        fifteen_ma5 = moving_average(res1['data'], 0, 5, 1)
        fifteen_ma10 = moving_average(res1['data'], 0, 10, 1)
        res2 = get_kline(symbol, '5min', 10)
        five_ma5 = moving_average(res2['data'], 0, 5, 1)
        five_ma10 = moving_average(res2['data'], 0, 10, 1)
        # print(res2)
        res3 = get_kline(symbol, '1min', 30)
        three_ma5 = moving_average(res3['data'], 0, 15, 3)
        three_ma10 = moving_average(res3['data'], 0, 30, 3)
        # print(res3)
        if fifteen_ma5 < fifteen_ma10:
            if check_account() > 0.0 and check_account() < 1.0:
                print('sell all')
                sell(1, symbol)
            if five_ma5 > five_ma10:
                if three_ma5 > three_ma10 and check_account() == 0.0:
                    print('buy')
                    cost_price = buy(1, symbol)
                if (three_ma5 < three_ma10 and check_account() == 1.0
                        and price_difference(cost_price, float(res3['data'][0]['close'])) == 1):
                    print('loss')
                    sell(1, symbol)
            elif five_ma5 < five_ma10 and check_account() > 0.0:
                sell(1, symbol)
                print('sell all')
        elif fifteen_ma5 > fifteen_ma10:
            if three_ma5 < three_ma10 and check_account() == 1.0:
                sell(0.25, symbol)
                print('rest 75%')
            if five_ma5 < five_ma10 and check_account() > 0.5:
                sell(0.5, symbol)
                print('rest 30%')

        #   if (res1['data'][0]['close'] > res1['data'][0]['open']
        #   and res1['data'][0]['high'] > res2
        #   and res1['data'][1]['high'] < res3):
        #    print('1')
        #    print(res2)
        #    print (res1['data'][0])
        # order = send_order(per_amount, 'api', symbol, 'buy-market', 0)
        # print (order)
        # if order['status'] == 'ok':
        #     detail = order_matchresults(order['data'])
        #     cost_price = (per_amount + amount * cost_price)/(amount+float(detail['data'][0]['filled-amount']))
        #     amount += float(detail['data'][0]['filled-amount'])
        #     time.sleep(30)
        # if (res1['data'][0]['open'] > res1['data'][0]['close']
        # and res1['data'][0]['high'] < res2
        # and res1['data'][1]['high'] > res3):
        #    print('2')
        #    print(res2)
        #    print (res1['data'][0])
        # if (amount != 0.0 and (res1['data'][0]['high'] > cost_price * 1.01
        # or res1['data'][0]['low'] < cost_price * 0.99)):
        #     order = send_order(amount, 'api', symbol, 'sell-market', 0)
        #     print (order)
        #     if order['status'] == 'ok':
        #        cost_price = 0.0
        #        amount = 0.0
