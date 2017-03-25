# coding:utf-8
__author__ = 'love_huan'
import numpy

a = numpy.array([1, 2, 3, 4, 5])
b = numpy.array([[1, 2, 3, 4], [1, 1, 1, 1]])
c = b.reshape((4,-1))
print(c)


