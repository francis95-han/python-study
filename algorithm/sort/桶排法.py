#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
桶式排序
有N个整数，范围在0-M，对其进行排序，该示例中N由你决定，M=1000
对大小为M的count数组初始华为0,Ai输入Count[Ai]中
复杂度O(M+N)
"""
import time


def tong_pai():
    for a in range(0, 1000):
        for b in range(1, count[a] + 1):
            print(a, end=' ')


# 对大小为M的count数组初始华为0
count = []
for i in range(0, 1000):
    count.append(0)
# print(a)
# Ai输入,Count[Ai]增1
num = input('输入你所需要排序的数量')
for i in range(0, int(num)):
    t = int(input('请输入数据'))
    if t < 1000:
        count[t] += 1
    else:
        print("您输入的数据不符合该算法")
        exit()
start = time.clock()
tong_pai()
end = time.clock()
print("该程序运行桶排时间为:%fs" % (end - start))
