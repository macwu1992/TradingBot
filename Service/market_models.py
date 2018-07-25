#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:Service
NAME:market_models
AUTHOR:Tong
Create Date:2018/5/6
'''

from django.db import models

class Accounts(models.Model):
    id = models.FloatField(max_length=100, blank=False, default=0)
    state = models.CharField(max_length=100, blank=False, default='')
    type = models.CharField(max_length=100, blank=False, default='')

    class Meta:
        ordering = ('created',)