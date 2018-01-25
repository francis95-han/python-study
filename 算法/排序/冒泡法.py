#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = []
n = int(input('请输入总共有多少数据'))
for i in range(0,n):
    print("请输入第%s个数据" % (i+1) )
    t = int(input())
    a.append(t)

for i in range(0,n-1):
    for j in range(0,n-1):
        if a[j] < a[j+1]:
            t=a[j]
            a[j] = a[j+1]
            a[j+1]=t

for i in range(0,n):
    print(a[i])