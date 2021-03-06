# -*- coding:utf-8 -*-
import urllib2
import urllib
import json


def main(filename,resultname):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    with open(filename) as f:
        with open(resultname, "w") as result:
            input = f.read()
            try:
                input = json.loads(input)
            except ValueError, e:
                print u"input.json存在格式错误, 请参考:"
                print str(e)
                return
            i = 0
            for ins in input:
                i = i + 1
                print u"正在测试第%d个REST接口:%s" % (i, ins["url"])
                result.write(u"第%d个REST接口:\n" % i)
                result.write(u"url : %s \n" % ins["url"])
                # URL参数赋值
                req = urllib2.Request(ins["url"])
                #print ins["body"]
                for (k, v) in ins["body"].items():
                    if type(v) == dict:
                        ins["body"][k] = json.dumps(v)
                        #print("pass")
                    elif type(v)==list:
                        ins["body"][k] = json.dumps(v)
                        #print("pass2")
                    else:
                        ins["body"][k] = json.dumps(v)
                        #print("pass3")
                req.add_data(urllib.urlencode(ins["body"]))
                #print ins["body"]
                #body_test='resourceDetail=%5B%7B%27masterResourceIds%27%3A+%27c84bb0ddbfd942a28a04224581fb9296%27%2C+%27userId%27%3A+%279cd636bdb01b451db27be0e04feebd02%27%2C+%27accountId%27%3A+%279b5ec7efe1b245c388fa008447f9ec2c%27%7D%5D'
                #req.add_data(body_test)
                #print type(ins["body"])
                #print  urllib.urlencode(ins["body"])
                if ins["header"]:
                    for (k, v) in ins["header"].items():
                        req.add_header(k, v)
                if ins.get("method"):
                    req.get_method = lambda: ins["method"].upper()
                else:
                    req.get_method = lambda: "POST"
                try:
                    content = urllib2.urlopen(req).read()
                    if ins.get("expect"):
                        if ins["expect"] in content:
                            print u"测试通过"
                            result.write(u"结果: 测试通过 \nexpect: %s \nresponse: %s" % (ins["expect"], content))
                        else:
                            print u"!!!测试失败!!!"
                            print u"expect: %s" % ins["expect"]
                            print u"response: %s" % content
                            result.write(u"结果: 测试失败 \nexpect: %s \nresponse: %s" % (ins["expect"], content))
                    else:
                        print u"未定(无expect)"
                        result.write(u"结果: 未定(无expect) \nresponse: %s" % content)
                except urllib2.URLError:
                     print "测试失败：请检查ip、端口是否正确"
                except:
                     print "测试失败"
                print "=" * 10
                result.write("\n\n" + "=" * 10 + "\n\n")
    print u"测试结束, 详情请看result.txt"

if __name__ == '__main__':
    main("input_createOrder.json","result_create.txt") #yes repeatable
    #main("input_newTrialOrder.json","result_newTrialOrder.txt") #yes repeatable
    #main("input_renew.json","result_renew.txt")   # yes one
    #main("input_refund.json","result_refund.txt")  #yes one
    #main("input_update.json","result_update.txt")  # yes  one
    #main("input_normalToOndemand.json","result_normalToOndemand.txt")  # yes repeatable
    #main("input_bill.json","result_bill.txt")  #yes reapeatable  problem
    #main("input_renewOrderBatch.json","result_renewOrderBatch.txt") #yes reapeatable
    #main("input_refundOrderBatch.json","result_refundOrderBatch.txt") #yes  reapeatable
    #main("input_search.json","result_search.txt") #yes reapeatable



