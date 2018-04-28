#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 2018/4/19 19:38"""

from ctypes import *
from debugger.my_debugger_defines import *

kernel32 = windll.kernel32


class debugger():
    def __index__(self):
        pass

    def load(self, path_to_exe):
        # 参数dwCreationFlags中的标志位控制着进程的创建方式。你若希望新创建的金长城独占一个新的控制台窗口，
        # 而不是于父进程公用同一个控制台，你可以加上CREATE_NEW_CONSOLE
        creation_flags = DEBUG_PROCESS

        # 实例化之前定义的结构体
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        # 在一下两个成员变量的共同作用下，新建进程将在一个单独的窗体中被显示，你可以通过改变结构体STARTUPINFO中的各成员变量的值来控制debugee进程的行为
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        # 设置结构体STARTUPINFO中的成员变量，
        # cb的值用以表示结构体本身的大小
        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)):
            print("[*] We have successfully launched the process")
            print("[*] PID: %d" % process_information.dwProcessId)
        else:
            print("[*] Error: 0x%08x." % kernel32.GetLastError())
