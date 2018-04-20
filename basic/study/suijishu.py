#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random    #加载随机数模块
# 定义生成随机字符串函数
global str,a  #定义全局变量

def create(num):
    global str  # 此函数中使用的str为全局变量
    Dic={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z',27:' '}
    str = ""
    while num:
        a = random.randint(1,27)  #生成1-27之间的随机数
        str+=Dic[a]
        # print(str)
        num-=1
    # print(str)
#验证函数
def yanzheng():
    global str,a  # 此函数中使用的str为全局变量
    # print(str)
    str_yanzheng="me"#thinks it is a weasel"
    # print(str==str_yanzheng)
    if(str in str_yanzheng):
        a=1
    else:
        a=0
i=1
a=0
while(a==0):
    create(2)
    yanzheng()
    # print(a)
    i+=1
    print('.',end='')
    # if(i>10):
    #     exit()
print(i)