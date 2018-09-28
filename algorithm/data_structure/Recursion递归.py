#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
from timeit import Timer   #引用 Python 中的 timeit 模块。这个 timeit 模块是被设计成在一个持续稳定的环境中，尽可能使用与计算机操作系统相似的计时机制，让 Python 的开发者实现跨平台运行时间的测量
#
# 迭代求和

def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum
def test1():
    list_sum([1,3,5,7,9])
t1 = Timer("test1()", "from __main__ import test1")    #定义一个Timer对象
print("concat ", t1.timeit(number=1000), "milliseconds")        #默认运行次数为1000次

# 递归求和
def list_sum(num_list):
    if len(num_list) == 1:
        print(num_list[0])
        return num_list[0]

    else:
        print(num_list[0],end=" ")
        print("list_sum",end=" ")
        print(num_list[1:])
        return num_list[0] + list_sum(num_list[1:])
def test2():
   print(list_sum([1,3,5,7,9]))

t2 = Timer("test2()", "from __main__ import test2")
print("concat ", t2.timeit(number=1000), "milliseconds")
test2()

'''
递归算法必须有个基本结束条件
递归算法必须改变自己的状态并向基本结束条件演进
递归算法必须递归地调用自身
'''

# 递归求解阶乘

def jiecheng(num):
    result=0
    if num>1:
        result=num*jiecheng(num-1)
    else:
        result=num
    return result
print(jiecheng(4))