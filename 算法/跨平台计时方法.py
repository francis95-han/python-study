#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from timeit import \
    Timer
# 引用 Python 中的 timeit 模块。这个 timeit 模块是被设计成在一个持续稳定的环境中，尽可能使用与计算机操作系统相似的计时机制，让 Python 的开发者实现跨平台运行时间的测量


def test1():
    a = list(range(1000))


def test2():
    a = []
    for i in range(1000):
        a = a + [i]


def test3():
    a = [i for i in range(1000)]


def test4():
    a = []
    for i in range(1000):
        a.append(i)


t1 = Timer("test1()", "from __main__ import test1")  # 定义一个Timer对象
print("concat ", t1.timeit(number=1000), "milliseconds")  # 默认运行次数为1000次
t2 = Timer("test2()", "from __main__ import test2")
print("concat ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("concat ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("concat ", t4.timeit(number=1000), "milliseconds")
