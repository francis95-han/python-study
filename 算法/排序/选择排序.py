#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 算法复杂度O(n^2）
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        alist[fillslot],alist[positionOfMax]  = alist[positionOfMax],alist[fillslot]

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)