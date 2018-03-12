#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author zhangbohan.dell@gmail.com
# @create 2018-03-08 10:11

class game:

    def __init__(self):
        self.arr= (" ")
    def show(self,a):
        for i in range(1,50):
            if  i%a != 0 and i%10!=a:
                print(i,end=" ")
            else:
                print("-",end=" ")
        print()


if __name__ == "__main__":
    an = game()
    an.show(3)
    an .show(7)