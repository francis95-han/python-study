#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function: 蒙提霍尔三门问题
    @create 2018/9/27 10:09"""

import random


def MontyHall(Dselect, Dchange):
    Dcar = random.randint(1, 3)  # 随机等可能放置汽车
    if Dcar == Dselect and Dchange == 0:  # 一开始选中并且没有改变选择
        return 1
    elif Dcar != Dselect and Dchange == 0:  # 一开始没选中也没有改变选择
        return 0
    elif Dcar == Dselect and Dchange == 1:  # 一开始选中并且改变选择
        return 0
    else:  # 一开始没选中并且改变选择
        return 1


n = 10000
win = 0
for i in range(n):
    select = random.randint(1, 3)
    win += MontyHall(select, random.randint(0, 1))
print("不确认是够改变选择{}".format(float(win / n)))

win = 0
for i in range(n):
    select = random.randint(1, 3)
    win += MontyHall(select, 0)
print("确认不改变选择{}".format(float(win / n)))

win = 0
for i in range(n):
    select = random.randint(1, 3)
    win += MontyHall(select, 1)
print("确认改变选择{}".format(float(win / n)))
