# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/7 19:27

class Project:

    getProjectData = """select * from projectApi where name = '%s' """

    updateProjectData = """update projectApi set `last_actual`=\"%s\", `create_time`='%s', `status`='%s' where name = '%s' """