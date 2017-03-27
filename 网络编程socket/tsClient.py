# coding:utf-8
__author__ = 'love_huan'

from socket import *
HOST = 'localhost'
PORT = 21657
BUFIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data :
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFIZ)
    if not data:
        break
    print(data)

tcpCliSock.close()