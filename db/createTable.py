# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/7 15:09

class createTable:

    projectApi = """CREATE TABLE `projectApi` (
                    `id`  int NULL ,
                    `expect`  varchar(512) NULL ,
                    `type`  int NULL ,
                    `last_actual`  varchar(512) NULL ,
                    `name`  varchar(64) NULL ,
                    `create_time`  datetime NULL ,
                    `status` int NULL
                    )
                    ;"""