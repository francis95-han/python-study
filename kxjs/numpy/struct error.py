#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy 

persontype = numpy.dtype({
    'names':['name', 'age', 'weight'],
    'formats':['S32','i', 'f']})
a = numpy.array([("Zhang",32,75.5),("Wang",24,65.2)],dtype=persontype)
b = numpy.array([[0,1,2],[4,5,6],[7,8,9.1]],dtype = numpy.float32)
print(b)

