#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 2018/11/27 16:21"""

import random as rd
import requests
import csv
from pythonds.basic.queue import Queue
import os
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def createDeviceId():
    deviceId = "27113E8F-6F5F-4F1E-A842-D2AB5C737B80"
    device_id = ""
    string = "abcdefghigklmnopqrstuvwxyz0123456789"
    for i in range(0, len(string)):
        if i == 8 or i == 13 or i == 18 or i == 23:
            device_id += "-"
        else:
            a = rd.randint(0, len(string) - 1)
            device_id += string[a]
    return device_id


qu = []


def task_creater():
    a = 200
    for i in range(0, a):
        qu.append(createDeviceId().upper())


class Task(threading.Thread):
    def __init__(self, device_id, result):
        # 重写写父类的__init__方法
        super(Task, self).__init__()
        self.device_id = device_id
        self.result = result
        self.url = "http://119.253.83.253:2080/abtest/client/client/show"
        self.header = {"Host": "119.253.83.253:2080",
                       "user-agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}

    def run(self):
        self.task_runner(self.device_id, self.result)

    def task_runner(self, deviceId, result):
        print(deviceId)
        jsonstring = bytes(json.dumps({
            "appKey": "3e2c1f92c798462fb71f6152a428ffdc",
            "type": 1,
            "deviceId": deviceId
        }), "utf-8")
        res = requests.post(url=self.url, data=jsonstring, headers=self.header).text
        a = json.loads(res)
        self.result.enqueue(deviceId + "\t" + str(a.get("data")[0].get("value")))
        # i = 0
        # while i <= 3:
        #    try:
        #        res = requests.post(url=self.url,data=jsonstring,headers=self.header).text
        #    except Exception as e:
        #            print(u'[INFO] %s%s' % (e, deviceId))
        #            i += 1
        #    else:
        #        a=json.loads(res)
        #        self.result.enqueue(deviceId+"\t"+str(a.get("data")[0].get("value")))   


def test():
    executor = ThreadPoolExecutor(10)
    task_creater()
    Thread_list = []
    results = Queue()
    # 创建并启动线程

    for device_id in qu:
        p = Task(device_id, results)
        result = executor.submit(p.run())
    writeToCsv(results)


def writeToCsv(queue):
    path = "D:/test/abtest/"
    if not os.path.exists(path):
        os.makedirs(path)
    with open("D:/test/abtest/result.csv", 'w', newline='') as f:
        write = csv.writer(f)
        while not queue.isEmpty():
            strings = queue.dequeue()
            write.writerow([strings.split("\t")[0], strings.split("\t")[1]])


if __name__ == '__main__':
    start = time.time()
    test()
    end = time.time()

    print(end - start)
