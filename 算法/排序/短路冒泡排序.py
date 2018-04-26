#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 算法复杂度O(n^2）
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum = passnum - 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shortBubbleSort(alist)
print(alist)
