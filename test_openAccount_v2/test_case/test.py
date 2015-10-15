#!/usr/bin/env python

'''

Function:
@author: lina
To me :Believe yourself!
'''
import http.client
import json
#此代码在python3下面能正常运行
def curl(host="ip.taobao.com", port=80, method="POST", path="/service/getIpInfo.php?ip="):
    h1 = http.client.HTTPConnection(host, port)
    h1.request(method, path)
    return h1.getresponse().read().decode("utf-8")


data = curl("ip.taobao.com", 80, "POST", path="/service/getIpInfo.php?ip=" + "49.80.254.51")
json_data = json.loads(data)
print json_data