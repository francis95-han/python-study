#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 18-4-30 下午8:37"""

import socket

target_host = "127.0.0.1"
target_port = 80
# 建立一个socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 发送一些数据
client.sendto(("AAAAAABBBBBBVVVVV").encode(),(target_host,target_port))
# 接受一些数据
data,addr = client.recvfrom(4096)

print(data)
