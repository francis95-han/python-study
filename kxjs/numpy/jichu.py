# coding:utf-8
__author__ = 'love_huan'
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3, 4], [1, 1, 1, 1]])
c = b.reshape((4,-1))
print(c)


