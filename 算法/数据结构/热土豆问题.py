#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
热土豆问题也称作 Josephus 问题。这个故事是关于公元 1 世纪著名历史学家Flavius Josephus 的，传说在犹太民族反抗罗马统治的战争中， Josephus 和他的 39 个同胞在一个洞穴中与罗马人相对抗。当注定的失败即将来临之时，他们决定宁可死也不投降罗马。于是他们围成一个圆圈，其中一个人被指定为第一位然后他们按照顺时针进行计数， 每数到第七个人就把他杀死。传说中 Josephus 除了熟知历史之外还是一个精通于数学的人。他迅速找出了那个能留到最后的位置。最后一刻，他没有选择自杀而是加入了罗马的阵营。这个故事还有许多不同的版本。有些是以三为单位进行计数，有些则是让最后一个留下的骑马逃走。但不管是哪个版本，其核心原理都是一致的
'''

from pythonds.basic.queue import Queue

def HotPotato(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue
print(HotPotato(["Bill","David","Susan","Tom","Amy","ken"],8133222))