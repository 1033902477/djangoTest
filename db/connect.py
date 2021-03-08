# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/7 19:21

from django.db import connections

def localhost():
    cursor = connections['default']
    return cursor