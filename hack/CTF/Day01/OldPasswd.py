#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 2018/3/21 17:44"""

lis = 'abcdefghijklmnopqrstuvwxyz'
upperLis = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def charShift(string, width=1, times=25):
    for j in range(times):
        results = []
        for i in range(len(string)):
            if string[i].islower():
                results.append(lis[(lis.index(string[i]) + 1 + j) % len(lis)])
            elif string[i].isupper():
                results.append(upperLis[(upperLis.index(string[i]) + 1 + j) % len(upperLis)])
            else:
                results.append(string[i])
        yield ''.join(results)


string = 'XZSDMFLZ'
for i in charShift(string):
    print(i)
