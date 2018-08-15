#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 18-5-28 下午9:33"""
import paramiko
import socket
import sys
import threading

host_key = paramiko.RSAKey(filename='key.key')


def check_channel_request(kind, chanid):
    if kind == 'session':
        return paramiko.OPEN_SUCCEEDED
    return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        if username == 'root' and password == 'gj5846gj..':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


server = sys.argv[1]
ssh_port = int(sys.argv[2])
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket.bind((server, ssh_port))
    sock.listen(100)
    print("[*] Listening for neection ...")
    client, addr = sock.accept()
except Exception as e:
    print('[-] Listening failed: ' + str(e))
    sys.exit(1)
print('[+] Got a connection')

try:
    bh_session = paramiko.Transport(client)
    bh_session.add_server_key(host_key)
    SERVER = Server()
    try:
        bh_session.start_server(server=server)
    except paramiko.SSHException as e:
        print("[-] SSH negotion failed:" + str(e))
    chan = bh_session.accept(20)
    print('[+] Authenticated!')
    print(chan.recv(1024))
    chan.send('Welcome to bh_ssh')
    while True:
        try:
            command = input("Enter command :").strip('\n')
            if command != 'exit':
                chan.send(command)
                print(chan.recv(1024) + '\n')
            else:
                chan.send('send')
                print('exiting')
                bh_session.close()
                raise Exception('exit')
        except KeyboardInterrupt:
            bh_session.close()
except Exception as e:
    print('[-] Caught exception :'+str(e))
    try:
        bh_session.close()
    except:
        pass