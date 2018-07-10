#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 18-5-28 下午9:33"""
import socket, paramiko, threading, sys

host_key = paramiko.RSAKey(filename='key.key')


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

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
    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(host_key)
    SERVER = Server()
    try:
        bhSession.start_server(server=server)
    except paramiko.SSHException as e:
        print("[-] SSH negotion failed:" + str(e))
    chan = bhSession.accept(20)
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
                bhSession.close()
                raise Exception('exit')
        except KeyboardInterrupt:
            bhSession.close()
except Exception as e:
    print('[-] Caught exception :'+str(e))
    try:
        bhSession.close()
    except:
        pass