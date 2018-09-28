#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function: 分赌本问题
    @create 2018/9/27 11:00"""

import random

'''
:param n 赢钱所需要的局数
:param n1 第一个人已经赢得局数
:param n2 第二个人已经赢得局数
'''


def Bookies(n, n1, n2):
    for i in range(2 * n - n1 - n2 - 1):
        D = random.randint(1, 2)
        if D == 1:
            n1 += 1
        else:
            n2 += 1
        if n1 == n:
            return 1
        if n2 == n:
            return 2


n = 10000
win = 0
for i in range(n):
    if Bookies(3, 2, 1) == 1:
        win += 1
print("A获得赢钱的可能为{}".format(float(win / n)))
