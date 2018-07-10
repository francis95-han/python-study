#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 18-4-30 下午8:28"""

import socket

target_socket = "127.0.0.1"
target_port = 9000

# 建立一个socket对象   SOK_STREAM表明这将是一个TCP客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接客户端
client.connect((target_socket, target_port))

# 发送一些数据
client.send("GET /HTTP/1.1\r\nHost:baidu.com\r\n\r\n".encode())

# 接受一些数据
response = client.recv(4096)

print(response)
