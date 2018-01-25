#!/usr/bin/env python3
# -*- coding: utf-8 -*-

myDic = {'name': 'ZhangBohan', 'password': 'gj5846gj'}
print(myDic)
print(myDic.keys())
print(myDic.values())
print(myDic['name'])
for i in myDic:
    print(myDic[i], i)
"""
    [] mydict[‘key’] 返回key 这个键所对应的值，如果key 不存在，则会报
错
In key in mydict 如果key 这个键在字典中，那么就返回True，如果不在，
就返回False
del del mydict[‘key’] 在字典中移除key 这个键所对应的键值对
"""
