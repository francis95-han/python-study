#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author zhangbohan.dell@gmail.com
# @create 2018-03-08 12:14
import re
print(re.compile("[1-9][0-9]{4,14}").fullmatch("0111112"))