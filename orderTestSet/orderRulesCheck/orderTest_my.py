# -*- coding:utf-8 -*-
__author__ = 'wangjunfei'
import orderSubmitCheck
from orderTestSet.utils.orderAPI import orderAPI
from orderTestSet.utils.mult_output_orderAPI import mult_output_orderAPI

def test():
    ordertest=orderAPI("inputAndOutput.json")
    result1,result2= ordertest.getJson()
    print result2

def test2():
    ordertest2=mult_output_orderAPI("inputAndOutput.json")
    result1,result2=ordertest2.getJson();
    print result2

if __name__=="__main__":
    test2()

