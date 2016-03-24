# # -*- coding:utf-8 -*-
# __author__ = 'user'
# import chardet
# import  json
# # f = open('D:\\ctCloud\\2016\\python\\testAPI.py','r')
# # data = f.read()
# # print(chardet.detect(data))
#
# import os
# import  sys
# BASE_DIR = os.path.dirname(__file__) #获取当前文件夹的绝对路径
# #print BASE_DIR
# file_path = os.path.join(BASE_DIR, r'test') #获取当前文件夹内的Test_Data文件
# #print file_path
#
# currentPathName=os.getcwd() #当前路径
# print currentPathName
# parentPathName =os.path.abspath(os.path.join(currentPathName, os.pardir)) #上一级路径
# print parentPathName
# #path = os.path.abspath(os.path.dirname(""))
#     # Test_Data = open(file_path, "r") #读取文件
#     # for line in Test_Data:
#     #     print line
# #     # Test_Data.close() #关闭文件
# # t1='{"t1":"1","t2":"2"}'
# # t1_re=json.loads(t1)
# # t2='{"t3":3,"t4":4}'
# # t2_re=json.loads(t2)
# # t3={}
# # t3["output1"]=t1_re
# # t3["output2"]=t2_re
# # print t3
#
# import urllib
# import json
# a='{"resours":[{"a":1,"b":2}]}'
# a1='{"resours":{"self":"myself"},"resours3":2}'
# b=json.loads(a)
# b["resours"]=json.dumps(b["resours"])
# b3=json.dumps(b)
#
# b1=json.loads(a1)
# b4=json.dumps(b1)
#
#
# print b
# print b1
# print b3
# print b4
#
# print urllib.urlencode(b)
# print urllib.urlencode(b1)
for i in range(0,3,1):
    print i
list=("1","2")
print len(list)
