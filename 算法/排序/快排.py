#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quicakSort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quicakSort(lists, low, left - 1)
    quicakSort(lists, left + 1, high)
    return lists


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quicakSort(alist, 0, len(alist) - 1)
print(alist)
