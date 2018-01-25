# !/usr/bin/env python3
# -*- coding: utf-8 -*-

myList = [12, 135, 156, 473, 213]
myList2 = [123, 453, 12, 31, 111]
print(myList + myList2)
print(myList * 3)
print(len(myList))
print(11 in myList)
print(myList[1:4])  # 下标为1到下表为4（不包括下表为4）

'''
append alist.append(item) 在列表末尾添加一个新项
insert alist.insert(i,item) 在列表的某个位置插入一个项
pop alist.pop() 移除并返回列表的最后一项
pop alist.pop(i) 移除并返回列表的第i 项
sort alist.sort() 对列表进行排序
reverse alist.reverse() 反转列表
del del alist[i] 删除在该位置上的元素
index alist.index(item) 返回列表中第一个等于item 项的索引
count alist.count(item) 返回列表中有多少项的值等于item
remove alist.remove(item) 删除列表中第一个值等于item 的项
'''
myList.sort()
print(myList)
