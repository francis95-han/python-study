#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 2018/9/29 10:54"""

import random

array = list()


class P:
    def __init__(self, name, p, p1, i):
        self.name = name
        self.p = p
        self.p1 = p1
        self.i = i
        self.psurplus= self.getpsurplus(i)

    def getpsurplus(self, n):
        if n > 1:
                return 100 - (self.p + self.p1) * self.getpsurplus(n - 1)
        else:
            return 100 - self.p1 - self.p


def setting():
    i = input()
    for i in range(int(i)):
        a = int(input())
        b = int(input())
        aclass = P(i, a, b, i)
        array.__add__(aclass)


def length(n):
    p1= array[n].p * array[n].psurplus
    p2= array[n].p1 * array[n].psurplus
    return p1, p2


def func(select, n):
    for i in range(n):
        for i in length(n):
            if select - i <= 0:
                return i
        select = select - length(n)


select = random.randint(0, 100)
