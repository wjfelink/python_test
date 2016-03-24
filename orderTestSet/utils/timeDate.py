# -*- coding:utf-8 -*-

import datetime

def getCurrentDateTime():
    #获得当前时间
    now = datetime.datetime.now() # ->这是时间数组格式
    #转换为指定的格式:
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime