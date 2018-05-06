#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:Rest_Service
NAME:Serializers
AUTHOR:Tong
Create Date:2018/5/6
'''
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')