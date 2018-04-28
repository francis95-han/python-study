#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from pythonds.basic.deque import Deque     从pythonds中获取Dueue
"""
Deque() 创建一个空双端队列，无参数，返回值为 Deque 对象。
addFront(item) 在队首插入一个元素，参数为待插入元素，无返回值。
addRear(item) 在队尾插入一个元素，参数为待插入元素，无返回值
removeFront() 在队首移除一个元素，无参数，返回值为该元素。双端队列会被改变。
removeRear() 在队尾移除一个元素，无参数，返回值为该元素。双端队列会被改变。
isEmpty() 判断双端队列是否为空，无参数，返回布尔值。
size() 返回双端队列中数据项的个数，无参数，返回值为整型数值。
"""


class deque:
    def __init__(self):
        self.items = []

    def addFrontItem(self, item):
        self.items.append(item)

    def addRearItem(self, item):
        self.items.insert(0, item)

    def removeFrontItem(self):
        return self.items.pop()

    def removeRearItem(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


'''
d=Deque() [] Deque 对象
d.isEmpty() [] True
d.addRear(4) [4]
d.addRear(‘dog’) [‘dog’,4]
d.addFront(‘cat’) [‘dog’,4, ‘cat’]d.addFront(True) [‘dog’,4, ‘cat’,True]
d.size() [‘dog’,4, ‘cat’,True] 4
d.isEmpty() [‘dog’,4, ‘cat’,True] False
d.addRear(8.4) [8.4,‘dog’,4, ‘cat’,True]
d.removeRear() [‘dog’,4, ‘cat’,True] 8.4
d.removeFront() [‘dog’,4, ‘cat’] True
'''
d = deque()
print(d.isEmpty())
d.addRearItem(4)
d.addRearItem('dog')
d.addFrontItem('cat')
d.addFrontItem(True)
print(d.size())
print(d.isEmpty())
d.addRearItem(8.4)
print(d.removeRearItem())
print(d.removeFrontItem())
