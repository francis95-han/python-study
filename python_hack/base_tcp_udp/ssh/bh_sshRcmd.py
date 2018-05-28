#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 18-5-28 下午9:11"""

import threading, paramiko, subprocess


def ssh_command(ip, user, password, command):
    client = paramiko.SSHClient()
    # client.load_host_keys('/home/icecap/known_hosts')
    # paramiko支持如上密钥认证
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return


ssh_command('139.199.21.130', 'root', 'gj5846gj..', 'id')
