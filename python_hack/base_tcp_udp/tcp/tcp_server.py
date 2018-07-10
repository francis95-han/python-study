#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 18-4-30 下午8:45"""

import socket
import threading

bing_ip = "0.0.0.0"
bing_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bing_ip, bing_port))
server.listen(5)
print("[*]listeing on %s:%d" % (bing_ip, bing_port))


# 这是客户端处理线程
def handle_client(client_socket):
    # 打印出客户端发送的内容
    request = client_socket.recv(1024)
    print("[*] Receiced %s" % request)
    #     返还一个数据包
    client_socket.send("ACK!".encode())
    client_socket.close()


while True:
    client, attr = server.accept()
    print("[*] Accepted connection from {0}:{1}".format(attr[0], attr[1]))
    # 挂起客户端线程，处理传入的数据
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
