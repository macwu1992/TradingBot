#!/usr/bin/env python
# -*- coding: utf-8 -*-

import HuobiServices as service

print(service.get_balance())
print(service.get_trade('eosbtc'))