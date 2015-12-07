# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

persontype = np.dtype({
    'names':['name', 'age', 'weight'],
    'formats':['S32','i', 'f']})
a = np.array([("Zhang",32,75.5),("Wang",24,65.2)],dtype=persontype)

b = np.array([[0,1,2],[4,5,6],[7,8,9.1]],dtype = np.float32)
print(b)

