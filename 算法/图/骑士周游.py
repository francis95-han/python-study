#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pythonds.graphs import Graph


# 建立一个 n*n 棋盘对应的完整图
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, column, board_size):
    return (row * board_size) + column


# genLegalMoves 函数（代码 7.7）获取骑士当前的位置并生成所有八个走棋步骤。
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


# legalCoord辅助函数确保任何个步骤不会超出棋盘（会导致 IndexError ）
def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
