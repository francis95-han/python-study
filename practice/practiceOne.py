#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 2018/3/19 16:28
    @demand:统计字符串中每个字符的次数。String  s="adsdfsdfsdfse1231234sdfsdf";"""

s = "adsdfsdfsdfse1231234sdfsdf"
set = {}
for i in s:
    if set.get(i, None) == None:
        set[i] = 1
    else:
        set[i] += 1
print(set)
