# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 算法复杂度O(n^2）


def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[positionOfMax]:
                positionOfMax = location
        a_list[fill_slot], a_list[positionOfMax] = a_list[positionOfMax], a_list[fill_slot]


aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(aList)
print(aList)
