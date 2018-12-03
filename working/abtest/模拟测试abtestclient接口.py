#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function: 测试abtest系统客户接口频率访问是否正常使用
    @create 2018/11/27 16:21"""


import random as rd
import urllib.request as request
import urllib.response as response
import urllib.parse as pa
import json
import csv


def createDeviceId():
    deviceId = "27113E8F-6F5F-4F1E-A842-D2AB5C737B80"
    device_id = ""
    string = "abcdefghigklmnopqrstuvwxyz0123456789"
    for i in range(0,len(string)):
        if i == 8 or i == 13 or i == 18 or i == 23:
            device_id+="-"
        else:
            a = rd.randint(0,len(string)-1)
            device_id+=string[a]
    return device_id

def test():
    a = 10000
    result =[]
    result.append(["次数","deviceId","结果"])
    for i in range(0,a):
        print(i)
        url = "http://119.253.83.253:2080/abtest/client/client/show"
        deviceId=createDeviceId().upper()
        #print(deviceId)
        jsonstring = bytes(json.dumps({
              "appKey": "3e2c1f92c798462fb71f6152a428ffdc",
              "type": 1,
              "deviceId": deviceId
            }),"utf-8")
        #print(jsonstring)
        header={
            "Accept-Encoding":" gzip, deflate",
            "Accept-Language":" zh-CN,zh;q=0.9",
            "Connection":" keep-alive",
            "Content-Type":" application/json",
            "Cookie":" JSESSIONID=B37BF3330E59606A1FDACFD515F06618",
            "Host":" 119.253.83.253:2080",
            "Origin":" http://119.253.83.253:2080",
            "Referer":" http://119.253.83.253:2080/abtest/client/swagger-ui.html",
            "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
        req = request.Request(url=url,data=jsonstring,headers=header)
        res_data = request.urlopen(req)
        res = res_data.read()
        a =json.loads(res.decode("utf-8"))
        result.append([str(i),deviceId,a.get("data")[0].get("value")])
    writeToCsv(result)
        

def writeToCsv(list):
    with open("D:/test/abtest/result.csv" ,'w', newline='') as f:
        write =csv.writer(f)
        for row in list:
            write.writerow(row)
if __name__ == '__main__':
    test()