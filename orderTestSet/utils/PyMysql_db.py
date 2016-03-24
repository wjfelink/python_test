# -*- coding:utf-8 -*-

import PyMysql

def getDbData(host='192.168.13.20',port=3305,user='portal',passwd='portal.ctyun',db='portal_0224',sqltext= "SELECT * FROM master_order  where master_order_no=20160321164127330099 "):
    mysql = PyMysql.PyMysql()
    mysql.newConnection(host=host,port=port,user=user, passwd=passwd,db=db)
    # #定义sql语句
    lines ,cur = mysql.execute(sqltext,mode=PyMysql.DICTCURSOR_MODE)
    # #提取数据
    data = mysql.fetch_executeresult(cur, mode=PyMysql.FETCH_MANY, rows=20)
    #关闭连接
    mysql.closeConnnection()
    #print data
    return  data
#打印
if __name__ == '__main__':
    getDbData(sqltext="select *  from  master_order limit 10")

