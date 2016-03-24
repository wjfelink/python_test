# -*- coding:utf-8 -*-
import urllib2
import urllib
import json
import cookielib

auth_url = 'http://life.ctyun.com.cn/admin/ajax/userLogin'
takeorder_url = 'http://life.ctyun.com.cn/ajax/takeOrder'
# 登陆用户名和密码
data={"userPhone": "18133847059", "userPassword": "123"}
# urllib进行编码
#post_data=urllib.urlencode(data)
post_data=json.dumps(data)
# 发送头信息

headers ={"Content-type": "application/json", "Accept": "application/json, text/javascript, */*; q=0.01"}
# 初始化一个CookieJar来处理Cookie

cookieJar=cookielib.CookieJar()
# 实例化一个全局opener

opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))

# 登陆并获取cookie
req=urllib2.Request(auth_url,post_data,headers)
result = opener.open(req)
print "Login return result:",result.read()


# 访问api 自动带着cookie信息 获取数据
order_postData={"addressId": 2, "id": "2016032313471215353631"}
req2=urllib2.Request(takeorder_url,json.dumps(order_postData),headers)
result2 = opener.open(req2)
apiResult=result2.read()
# 显示结果
print "API Return data:",apiResult
if  "订餐成功"  in apiResult:
    print "订餐成功"
elif    "该用户已订餐完成，请勿重复下单" in apiResult:
    print "已订餐成功，请勿重复下单"
else:
    print "订餐失败"


