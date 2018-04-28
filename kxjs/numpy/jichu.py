#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy

a = numpy.array([1, 2, 3, 4, 5])
b = numpy.array([[1, 2, 3, 4], [1, 1, 1, 1]])
c = b.reshape((2, -1))
print(c)


