#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

from mayavi import mlab


def main():

     data = [[0 for y in xrange(100)] for x in xrange(100)] #data是一个100 * 100的二维数组

     factor = math.pi / 100;

     for x in xrange(100):

         for y in xrange(100):

             data[x][y] = 50 * math.cos((x+y) * factor)

     mlab.surf(data)     #绘制3D数据图

     mlab.show()         #显示出来

     return 0

if __name__ == '__main__':

     main()
