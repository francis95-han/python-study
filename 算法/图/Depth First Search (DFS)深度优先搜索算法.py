#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pythonds.graphs import Graph, Vertex
def knightTour(n,path,u,limit):  #n ，当前树的深度； path ，这个节点前所有已访问的点的列表； u ，我们能够探索的点； limit ，搜索总深度限制
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
        if not done: # prepare to backtrack
            path.pop()
            u.setColor('white')
        else:
            done = True
        return done