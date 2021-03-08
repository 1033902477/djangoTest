# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/7 19:28

from .sql import Project
from ..connect import localhost

# 获取接口所需要的的期望数据
def getApiExpect(name):
    cursor = localhost().cursor()
    cursor.execute(Project.getProjectData % (name))
    result = cursor.fetchone()
    cursor.close()
    return result[1]

def updateApiRestul(lastActual, createTime, status, apiName):
    cursor = localhost().cursor()
    try:
        cursor.execute(Project.updateProjectData % (lastActual, createTime, status, apiName))
        localhost().commit()
        cursor.close()
    except Exception:
        localhost().rollback()
        return Exception('update数据异常')