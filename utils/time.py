# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/7 20:48
import time
import datetime

class Time:

    def currentTime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def dateTime(self, dt):
        dtstamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(datetime.datetime.timestamp(dt)))
        return dtstamp