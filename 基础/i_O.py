#!/usr/bin/env python3
# -*- coding: utf-8 -*-

aName=input("please input your name ")
print(type(aName))
age=input("please input your age ")
age=float(age)
print(age)

print("hello","world","!!",sep="@@@",end="***")
print("%s is %d years old." % (aName, age))

'''
d, i 整型
u 无符号整型
f 浮点型，如m.ddddd
e 浮点型，如m.ddddde+/-xx
E 浮点型，如m.dddddE+/-xx
g 指数比-4 小或比5 大时使用%e，否则使用%f
c 单字符
s 字符串或者是能通过str()转为字符串的数据
% 输入一个%


number %20d 变量值占据20 个字符宽度
- %-20d 变量值占据20 个字符宽度，左对齐
+ %+20d 变量值占据20 个字符宽度，右对齐
0 %020d 变量值占据20 个字符宽度，前置“0”
. %20.2f 变量值占据20 个字符宽度，且保留两位小数
(name) %(name)d 从字典中取key 为name 的值放在此处
'''
itemDic={"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%itemDic)