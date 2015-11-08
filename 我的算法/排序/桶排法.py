# coding:utf-8
__author__ = "love_huan"
a = []

for i in range(0, 1000):
    a.append(0)
# print('shuju')
num = raw_input('输入你所需要排序的数量')

for i in range(0, int(num)):
    t = int(raw_input('请输入数据'))
    a[t] += 1
for i in range(0, 1000):
    for j in range(1, a[i] + 1):
        print(i)
