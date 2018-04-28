#!/usr/bin/env python3
# -*- coding: utf-8 -*-

myDic = {'name': 'ZhangBohan', 'password': 'gj5846gj'}
print(myDic)
print("keys：",myDic.keys())
print("valuse:",myDic.values())
print("items：",myDic.items())
print(myDic['name'])
for i in myDic:
    print( i,"is",myDic[i])

print(myDic.get('asd'))
print(myDic.get('asd','no this key'))
"""
# [] mydict[‘key’] 返回key 这个键所对应的值，如果key 不存在，则会报 错
# In key in mydict 如果key 这个键在字典中，那么就返回True，如果不在，就返回False
# del del mydict[‘key’] 在字典中移除key 这个键所对应的键值对
#  keys adict.keys() 以列表的形式返回adict 中的所有键(key)
# values adict.values() 以列表的形式返回adict 中的所有值(value)
# items adict.items() 以列表的形式返回adict 中的所有键值对，列表的每个元素是包含键和值的元组
# get adict.get(key) 返回key 所对应的值，如果key 不存在，就返回None
# get adict.get(key,alt) 返回key 所对应的值，如果key 不存在，就返回alt
操作复杂度
复制 O(n)
访问 O(1)赋值 O(1)
删除 O(1)
包含（in） O(1)
迭代 O(n)
"""