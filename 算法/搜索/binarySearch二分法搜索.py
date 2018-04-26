#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二分法搜索 算法复杂度O(log n）
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))


# 递归实现二分法搜索 Python的切片操作实际上是O(k)。这意味着二分搜索使用切片将不会运行严格的对数时间。幸运的是这可以通过列表的开始和结束索引值补救
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
    if alist[midpoint] == item:
        return True
    else:
        if item < alist[midpoint]:
            return binarySearch(alist[:midpoint], item)
        else:
            return binarySearch(alist[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
