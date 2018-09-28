#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 树是节点和连接节点的边的集合
# 有一个节点是根节点；
# 除了根节点外的每一个节点 n，都通过一条边与另一个节点 p 相连， p 是 n 的父节点；
# 可以沿着唯一的路径从根节点到达每个节点；
# 如果这个树的每个节点都至多有两个子节点，我们称它为二叉树
# 列表实现
def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]
x = BinaryTree('a')
insertLeft(x,'b')
insertRight(x,'c')
insertRight(getLeftChild(x),'d')
insertRight(getRightChild(x),'f')
insertLeft(getRightChild(x),'e')
print(x)

#           a
#       b   |   c
#       d   | f |  e
#
# r = BinaryTree(3)
# insertLeft(r, 4)
# insertLeft(r, 5)
# insertRight(r, 6)
# insertRight(r, 7)
# l = getLeftChild(r)
# print(l)
# setRootVal(l, 9)
# print(r)
# insertLeft(l, 11)
# print(r)
# print(getRightChild(getRightChild(r)))


#
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())
