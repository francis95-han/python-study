#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Fraction:
    def __init__(self,top,bottom):   # self 是一个特殊的参数，都可以用来作为参考返回对象本身。它必须是第一个正式参数
        self.num=top
        self.den=bottom
    def show(self):                 #print
        print(self.num,"/",self.den)
    def getNum(self):
        print(self.num)
    def getDen(self):
        print(self.den)
    def __str__(self):#__str__是一种方法来将对象转为字符串
        return str(self.num)+'/'+str(self.den)
    def __add__(self, other):       #+
        newnum=self.num*other.den+other.num*self.den
        newden=self.den*other.den
        commom=gcd(newden,newnum)
        return str(newnum//commom)+'/'+str(newden//commom)
    def __sub__(self,other):
        newnum = self.num * other.den - other.num * self.den
        newden = self.den * other.den
        commom = gcd(newden, newnum)
        return str(newnum // commom) + '/' + str(newden // commom)

    def __eq__(self, other):        #=
        ###通分判断方法
        # self_common=gcd(self.num,self.den)
        # new_self=str(self.num//self_common)+'/'+str(self.den//self_common)
        # other_common = gcd(other.num, other.den)
        # new_other = str(other.num // other_common) + '/' + str(other.den // other_common)
        # return new_other==new_self
        ###方法二
        firstnum=self.num*other.den
        secondnum=self.den*other.num
        return firstnum==secondnum
    def __gt__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum > secondnum
    def __le__(self, other):    #<=
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum or firstnum<secondnum
    def __mul__(self, other):   #*
        newnum=self.num*other.num
        newden=self.den*other.den
        commom = gcd(newden, newnum)
        return str(newnum // commom) + '/' + str(newden // commom)
    def __truediv__(self, other):  #/
        newnum = self.num * other.den
        newden = self.den * other.num
        commom = gcd(newden, newnum)
        return str(newnum // commom) + '/' + str(newden // commom)

def gcd(m, n):      #欧几里得算法查找最大公约数
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
        return n

myfraction=Fraction(3,5)
myfraction.getNum()
myfraction.getDen()
myfraction2=Fraction(2,7)
print(myfraction)
myfraction.show()
print(myfraction+myfraction2)
print(myfraction2==myfraction)
print(myfraction<=myfraction)
print(myfraction*myfraction2)
print(myfraction/myfraction2)
print(myfraction-myfraction2)

