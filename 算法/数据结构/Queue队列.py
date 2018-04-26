#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Queue()创建一个空队列对象，无需参数，返回空的队列；
enqueue(item)将数据项添加到队尾，无返回值；
dequeue()从队首移除数据项，无需参数，返回值为队首数据项；
isEmpty()测试是否为空队列，无需参数，返回值为布尔值；
size()返回队列中的数据项的个数，无需参数。

q=Queue() [] Queue 对象q.isEmpty() [] True
q.enqueue(4) [4]
q.enqueue(‘dog’) [‘dog’,4]
q.enqueue(True) [True,‘dog’,4]
q.size() [True,‘dog’,4] 3
q.isEmpty() [True,‘dog’,4] False
q.enqueue(8.4) [8.4,True,‘dog’,4]
q.dequeue() [8.4,True,‘dog’] 4
q.dequeue() [8.4,True] ‘dog’
q.size() [8.4,True] 2
'''

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
    
if __name__ == "__main__":
    q=Queue()
    q.enqueue('h')
    q.enqueue('a')
    print(q.size())
    print(q.dequeue())
    print(q.size())
    print(q.dequeue())
    print(q.size)
    print(q.isEmpty())
    print('Yummy~')


