#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def create(smallest,largest):
    intSet=[]
    for i in range(smallest,largest+1): intSet.append(None)
    return intSet

def insert(intSet,e):
    intSet[e] = 1

def member(intSet,e):
    return intSet[e]==1


