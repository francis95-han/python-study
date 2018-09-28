#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
s.is_empty() [] Trues.push(4) [4]
s.push(‘dog’) [4,’dog’]
s.peek() [4,’dog’] ‘dog’
s.push(True) [4,’dog’,True]
s.size() [4,’dog’,True] 3
s.is_empty() [4,’dog’,True] False
s.push(8.4) [4,’dog’,True,8.4]
s.pop() [4,’dog’,True] 8.4
s.pop() [4,’dog’] True
s.size() [4,’dog’] 2


Stack()创建一个新的空栈。它不需要参数，并返回一个空栈。
Push(item)将新项添加到堆栈的顶部。它需要参数 item 并且没有返回值。
pop()从栈顶删除项目。它不需要参数,返回 item。栈被修改。
peek()返回栈顶的项，不删除它。它不需要参数。堆栈不被修改。
isEmpty()测试看栈是否为空。它不需要参数，返回一个布尔值。
size()返回栈的项目数。它不需要参数，返回一个整数
'''
class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self):
        return self.items.pop()


if __name__ == "__main__":
    # 初始化一个栈对象
    my_stack = Stack()
    # 把'h'丢进栈里
    my_stack.push('h')
    # 把'a'丢进栈里
    my_stack.push('a')
    # 看一下栈的大小（有几个元素）
    print(my_stack.size())
    # 打印栈顶元素
    print(my_stack.peek())
    # 把栈顶元素丢出去，并打印出来
    print(my_stack.pop())
    # 再看一下栈顶元素是谁
    print(my_stack.peek())
    # 这个时候栈的大小是多少？
    print(my_stack.size())
    # 再丢一个栈顶元素
    print(my_stack.pop())
    # 看一下栈的大小
    print(my_stack.size)
    # 栈是不是空了？
    print(my_stack.is_empty())
    # 哇~真好吃~
    print('Yummy~')

