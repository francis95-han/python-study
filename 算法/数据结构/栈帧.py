#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pythonds.basic.stack import Stack  # As previously defined
import time
r_stack = Stack()

#十进制转化
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.isEmpty():
        res = res + str(r_stack.pop())
    return res

start = time.clock()
print(to_str(1453, 2))
end = time.clock()
print(end-start)