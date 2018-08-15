#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-19 21:08:38
# @Author  : Bohan Zhang (zhangbohan.dell@gmail.com)
# @Link    : https://blog.csdn.net/ice_cap1995
# @Version : $Id$

import os
from ctypes import *
# msvcrt = cdll.msvcrt
# message_string = b"hello world!\n"
# msvcrt.printf( b"using c printf  :%s ",message_string)
#
#
# print(windll.kernel32)
#
msvcrt = cdll.msvcrt
# print(msvcrt)
#
# print(msvcrt.printf)
# msg_str = b"Hello world!\n"
# msvcrt.printf(b"Testing: %s", msg_str)
# # 强制刷新缓冲区，立即输出，
# # 若无此句，会导致下面的python语句输出结束了才输出下面的字符串
# msvcrt.fflush(0)
#
# # 构建并使用C 数据类型
# i = c_int(9)
# print(i)
# print(i.value)
#
# i.value = 1212;
# print(i.value)
#
# str_cp = c_char_p(b"learn python ctypes")
# print(str_cp)
# print(str_cp.value)
#
# str_cp = c_wchar_p("hello python")
# print(str_cp)
# print(str_cp.value)


# 按引用传参可以使用function(byref(parameter))
# byref(obj[, offset]) Returns a light-weight pointer to obj,
# which must be an instance of a ctypes type. offset defaults to zero,
# and must be an integer that will be added to the internal pointer value.
# byref(obj, offset) corresponds to this C code:
# (((char *)&obj) + offset)
# The returned object can only be used as a foreign function call parameter.
# It behaves similar to pointer(obj), but the construction is a lot faster.
num = c_int()
print("input a int number:")
msvcrt.scanf(b"%d", byref(num))
print(num.value)