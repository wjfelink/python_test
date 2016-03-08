# -*- coding:utf-8 -*-
import urllib2
import urllib
import json


def main():
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    with open("input.json") as f:
        with open("result.txt", "w") as result:
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
    main()
