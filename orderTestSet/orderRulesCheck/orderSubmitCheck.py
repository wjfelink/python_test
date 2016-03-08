# -*- coding:utf-8
import  os
import json
import unittest
from orderTestSet.utils.orderAPI import orderAPI

class orderSubmitCheck(unittest.TestCase):

    def setUp(self):
        ordertest=orderAPI("inputAndOutput.json")
        self.result1,self.result2= ordertest.getJson()
        #print( 'start by orderSubmitCheck...')

    # def tearDown(self):
    #     #print( 'end by orderSubmitCheck...')

    def test_isPriceRight(self):
        inputJson=self.result1
        outputJson=self.result2
        self.assertEqual(outputJson["statusCode"],800)
        #print "test_isPriceRight:测试OK"

    def test_isNotEqual(self):
        self.assertNotEqual("1","1")

