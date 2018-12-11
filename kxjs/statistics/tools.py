#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 2018/12/6 10:05"""

import numpy as np
import pandas as pd


np.random.seed(40)

coffee_full = pd.read_csv('coffee_dataset.csv')
coffee_red = coffee_full.sample(200) #this is the only data you might actually get in the real world.
coffee_red.head()
coffee_red[coffee_red['drinks_coffee'] == True]['height'].mean()
boot_means = []
for _ in range(10000):
    bootsample = coffee_full.sample(200, replace=True)
    mean = bootsample[bootsample['drinks_coffee'] == False]['height'].mean()
    boot_means.append(mean)

np.percentile(boot_means, 2.5), np.percentile(boot_means, 97.5)

