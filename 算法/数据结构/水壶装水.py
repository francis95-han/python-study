#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
# 水壶 自己的大小  往另一个壶中倒水  加水
class Kettle():
    def __init__(self, size):
        self.size = size
        self.water = 0

    def __add__(self, item):
        result = self.water + item.water
        if (result > self.size):
            result = self.size
        self.water = result

    def full(self):
        self.water = self.size


kettle3 = Kettle(3)
kettle4 = Kettle(4)
