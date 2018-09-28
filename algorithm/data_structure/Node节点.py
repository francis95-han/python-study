#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self,initdata):
        '''
        每个节点对象必须持有至少两条信息。首先，节点必须包含列表元素本身。我们将这称为该节点的“数据区”（data field）
        '''
        self.data = initdata
        self.next = None    #在构造器中，一个节点的对下一节点引用的初始赋值是 None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext