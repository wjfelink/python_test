# -*- coding:utf-8 -*-
# import MySQLdb
#
# # database
# def get (sql,param,host='192.168.13.20',port='3305',user='portal',password='portal.ctyun',database='portal_0224'):
#     try:
#         conn = mysql.connector.connect(host=host,port=port,user=user, password=password,database=database)
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute(sql,param)
#     except Exception as e:
#         pass
#     finally:
#         pass
#     return cursor.fetchall()

import MySQLdb
conn=MySQLdb.connect(host='192.168.13.20', port=3305,user='portal', passwd='portal.ctyun',db='portal_0224')
sqltext='SELECT * FROM master_order  where master_order_no=20160321164127330099'
cursor = conn.cursor()
cursor.execute(sqltext,mode=1)
row = cursor.fetchone()
print "server version:", row
print type(row)
cursor.close()
conn.close()