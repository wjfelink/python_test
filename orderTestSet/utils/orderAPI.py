# -*- coding:utf-8 -*-
__author__ = 'wangjunfei'

import urllib2
import urllib
import json
import os

class orderAPI:
    def __init__(self,jsonfilename):
        currentPathName,parentPathName=orderAPI.getJsonFilePath()
        self.path= os.path.join(currentPathName,jsonfilename)#"inputAndOutput.json")

    @classmethod
    def getJsonFilePath(cls):#只能读取一个输入一个输出
        currentPathName=os.getcwd() #当前路径
        parentPathName =os.path.abspath(os.path.join(currentPathName, os.pardir)) #上一级路径
        return currentPathName,parentPathName

    def getJson(self):
         with open(self.path) as f:
            input = f.read()
            try:
                input = json.loads(input)
            except ValueError, e:
                print u"input.json存在格式错误, 请参考:"
                print str(e)
                return
            for ins in input:
                if ins["type"]=="input":
                    self.inputResult=ins["body"]
                    continue
                # URL参数赋值
                req = urllib2.Request(ins["url"])
                for (k, v) in ins["body"].items():
                    if type(v) == dict:
                        ins["body"][k] = json.dumps(v)
                req.add_data(urllib.urlencode(ins["body"]))
                if ins["header"]:
                    for (k, v) in ins["header"].items():
                        req.add_header(k, v)
                if ins.get("method"):
                    req.get_method = lambda: ins["method"].upper()
                else:
                    req.get_method = lambda: "POST"
                try:
                    content = urllib2.urlopen(req).read()
                    if ins["type"]=="input":
                        self.inputResult=ins["body"]
                    elif  ins["type"]=="output":
                        self.outputResult=content
                    else:
                        print("json 结构输出错误")

                except:
                     print "测试失败：请检查ip、端口是否正确"
            return self.inputResult,json.loads(self.outputResult)

# if __name__ == '__main__':
#     testorderapi=orderAPI("/inputAndOutput.json")
#     result1,result2=testorderapi.getJson()
#     print type(result1),type(result2)
#     print str(result1),"\n",result2




