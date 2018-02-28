# coding : utf-8
__author__ = 'ZhangBohan'

from socket import *
from time import ctime

HOST = ''
PORT = 21657
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connect......')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connneceted from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))


