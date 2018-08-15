#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import socket
import threading


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s1=socket.socket(family,type)
    # family参数代表地址家族，可为AF_INET或AF_UNIX。AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信。
    # type参数代表套接字类型，可为SOCK_STREAM(流套接字，就是TCP套接字)和SOCK_DGRAM(数据报套接字，就是UDP套接字)。
    # 默认为family=AF_INET  type=SOCK_STREM
    # 返回一个整数描述符，用这个描述符来标识这个套接字
    try:
        server.bind((local_host, local_port))
        # server.bind(address)
        # 由AF_INET所创建的套接字，address地址必须是一个双元素元组，格式是(host,port)。host代表主机，port代表端口号。
        # 如果端口号正在使用、主机名不正确或端口已被保留，bind方法将引发socket.error异常。
        # 例: ('192.168.1.1',9999)
    except socket.error:
        print("[!!]Failed to listen on {0}:{1}".format(local_host, local_port))
        print("[!!] Check for other listening sockets or corrent permissions")
        sys.exit(0)
    print("[*] Listening on {0}:{1}".format(local_host, local_port))

    server.listen(5)
    # server.listen(backlog)
    # backlog指定最多允许多少个客户连接到服务器。它的值至少为1。收到连接请求后，这些请求需要排队，如果队列满，就拒绝请求。
    while True:
        client_socket, addr = server.accept()
        # connection, address = s1.accept()
        # 调用accept方法时，socket会时入“waiting”状态，也就是处于阻塞状态。客户请求连接时，方法建立连接并返回服务器。
        # accept方法返回一个含有两个元素的元组(connection,address)。
        # 第一个元素connection是所连接的客户端的socket对象（实际上是该对象的内存地址），服务器必须通过它与客户端通信；
        # 第二个元素 address是客户的Internet地址。
        print("[==>] Received incoming connection from {0}:{1}".format(addr[0], addr[1]))
        proxy_thread = threading.Thread(target=proxy_handler, args=(
            client_socket, remote_host, remote_port, receive_first))
        # 创建proxy_handler()线程
        proxy_thread.start()
        # 开启线程


def main():
    if len(sys.argv[1:]) != 5:
        # 判定参数是不是5个，不是提示用法，程序终止
        print(
            "Usage : ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]")
        print("Example ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)


# 16进制导出函数
def hexdump(src, length=16):
    result = []
    # python中str就是uniciode
    digits = 4 if isinstance(src, str) else 2
    for i in range(0, len(src), length):
        # python3中使用range代替xrange
        s = src[i:i + length]
        hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b"." for x in s])
        result.append(b"%04X %-*s %s" % (i, length * (digits + 1), hexa, text))
    print(b"\n".join(result))


# 对目标是本地主机的响应进行修改
def response_handler(buffer):
    # 执行包修改
    return buffer


# 对目标是远程主机的请求进行修改
def request_handler(buffer):
    # 执行包修改
    return buffer


def receive_from(connection):
    buffer = ""
    connection.settimeout(2)
    # sk.settimeout(timeout)
    #   设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，
    #   因为它们可能用于连接的操作（如 client 连接最多等待5s ）

    try:
        # 持续从缓存中读取数据直到没有数据或者超时
        while True:
            data = connection.recv(4096)
            # sk.recv(bufsize[,flag])
            #   接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。
            if not data:
                break
            buffer += data
    except BufferError:
        pass
    return buffer


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        remote_buffer = response_handler(remote_buffer)

        if len(remote_buffer):
            print("[<==] Sending {0} bytes to localhost.".format(len(remote_buffer)))
            client_socket.send(remote_buffer)
    #         sk.send(string[,flag])
    #  将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。
    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print("[==>] received {0} bytes from localhost.".format(len(local_buffer)))
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote")

        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            print("[<==] Received %d bytes from remote.".format(len(remote_buffer)))
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)

            print("[<==] Sent to localhost.")

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break


main()
