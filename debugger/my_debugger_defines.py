#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-16 15:12:26
# @Author  : Bohan Zhang (zhangbohan.dell@gmail.com)
# @Link    : https://blog.csdn.net/ice_cap1995
# @Version : $Id$


from ctypes import *

WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

# 常值定义
DEBUG_PROCESS = 0x00000001
CRRATE_NEW_CONSOLE = 0x00000010


# 定义函数CreateProcessA()所需要的结构体
class STARTUPINFO(Structure):
    _fields_ = [
        ("cb", DWORD),
        ("lpReserved", LPTSTR),
        ("lpDesktop", LPTSTR),
        ("lpTitle", LPTSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserveds", WORD),
        ("lpReserveds", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
    ]


class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
    ]
