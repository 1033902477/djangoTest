# !/usr/bin/env python3
# _*_ coding=utf-8 _*_
# author: liuqing
# dateTime: 2021/3/8 10:15
import yaml
from config.path import DBPATH

with open(DBPATH, encoding='utf-8', errors='ignore') as f:
    data = yaml.load(f.read(), Loader=yaml.FullLoader)

with open(data['path']['localPath'], encoding='utf-8', errors='ignore') as f:
    db = yaml.load(f.read(), Loader=yaml.FullLoader)['localhost']

ENGINE = db['ENGINE']
NAME = db['NAME']
USER = db['USER']
PASSWORD = str(db['PASSWORD'])
HOST = db['HOST']
PORT = db['PORT']