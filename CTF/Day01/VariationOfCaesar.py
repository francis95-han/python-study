#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function 凯撒密码
    @create 2018/3/22 9:38
    @demand 加密密文：afZ_r9VYfScOeO_UL^RWUc   格式：flag{ }
"""
import re

ONE_STRING = "afZ_r9VYfScOeO_UL^RWUc"


def translate(ONE_STRING):
    for item in ONE_STRING:
        print(ord(item), end=" ")
    print("\r\n")


translate(ONE_STRING)
translate("flag{}")


def resolve(ONE_STRING):
    for item_second in range(101):
        new = ""
        for item in range(ONE_STRING.__len__()):
            new += chr(ord(ONE_STRING[item]) + item_second + item)
        # result = re.match("^flag.*", new)
        # if result != None:
        #     print(result.group(0))
        print(new)

resolve(ONE_STRING)
