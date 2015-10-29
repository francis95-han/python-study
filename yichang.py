# coding:utf-8
__author__ = "love_huan"
x = None
try:
    x = input('请输入第一个数字')
    y = input('请输入第二个数字')
    print(x / y)
except (ZeroDivisionError, TypeError),e:
    print e
else:
    print '请继续'
finally:
    print('clean up')
    del x
# p160