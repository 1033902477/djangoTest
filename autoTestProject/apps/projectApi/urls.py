# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/7 19:51

from ..projectApi import views
from django.urls import path

urlpatterns = [path(r'comparison', views.ComparisonApi.as_view())]