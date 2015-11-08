# coding:utf-8
__author__ = 'love_huan'

a = []
def quicakSort(left,right):

    if left > right:
        return
    temp = a[left]
    while (left != right):
        while (a[right] >= temp and left < right):
            right -= 1
        while (a[left] <= temp and left > right):
            left += 1

        if (left < right):
            t = a[left]
            a[left] = a[right]
            a[right] = t

    a[left] = temp
    quicakSort(left,left-1)
    quicakSort(left+1,right)

n = input('请输入总共有多少数据')
for i in range(0,n):
    print("请输入第%s个数据" % (i+1) )
    t = input()
    a.append(t)
quicakSort(1,n)

for i in range(1,n):
    print(a[i])