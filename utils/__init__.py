# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/7 13:22

from .core.dataComparison import Comparison
from .time import Time

__all__ = ['Comparison', 'Time']

comparion = Comparison()
time = Time()