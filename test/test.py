# -*- coding:utf-8 -*-
__author__ = 'user'
import chardet

# f = open('D:\\ctCloud\\2016\\python\\testAPI.py','r')
# data = f.read()
# print(chardet.detect(data))

import os
import  sys
BASE_DIR = os.path.dirname(__file__) #获取当前文件夹的绝对路径
#print BASE_DIR
file_path = os.path.join(BASE_DIR, r'test') #获取当前文件夹内的Test_Data文件
#print file_path

currentPathName=os.getcwd() #当前路径
print currentPathName
parentPathName =os.path.abspath(os.path.join(currentPathName, os.pardir)) #上一级路径
print parentPathName
#path = os.path.abspath(os.path.dirname(""))
    # Test_Data = open(file_path, "r") #读取文件
    # for line in Test_Data:
    #     print line
    # Test_Data.close() #关闭文件