#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mayavi.mlab as mlab
from numpy import exp, sin, cos, tan, random, mgrid, ogrid, linspace, sqrt, pi
import numpy as np
import matplotlib.pyplot as plt

mlab.figure(fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))  # 更改背景色


# 添加matlab的peaks函数
def peaks(x, y):
    return 3.0 * (1.0 - x) ** 2 * exp(-(x ** 2) - (y + 1.0) ** 2) - 10 * (x / 5.0 - x ** 3 - y ** 5) * exp(
        -x ** 2 - y ** 2) - 1.0 / 3.0 * exp(-(x + 1.0) ** 2 - y ** 2)


s = np.random.rand(3, 3)
mlab.barchart(s)
mlab.vectorbar()
mlab.show()
x, y = np.mgrid[-5:5:20j, -5:5:20j]
s = peaks(x, y)  # peaks函数前面已经定义
mlab.barchart(x, y, s)
mlab.vectorbar()
mlab.show()
# x, y = np.mgrid[-5:5:70j, -5:5:70j]
# # 绘制peaks函数的等高线
# mlab.contour_surf(x, y, peaks, contours=9)
# mlab.colorbar()
# mlab.show()
x, y, z = ogrid[-5:5, -5:5, -5:5]
scalars = x * x * 0.5 + y * y + z * z * 2.0
mlab.contour3d(scalars, contours=6, transparent=True)
mlab.colorbar()
mlab.show()
