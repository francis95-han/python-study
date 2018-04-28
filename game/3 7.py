#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author zhangbohan.dell@gmail.com
# @create 2018-03-08 10:11


class game:

    def __init__(self):
        self.arr = (" ")

    def show(self, a):
        for i in range(1, 500):
            if i % a != 0 and i % 10 != a:
                print(i, end=" ")
            else:
                print("拍", end=" ")
        print()


if __name__ == "__main__":
    an = game()
    print(2,end="\n")
    an.show(2)
    print(3,end="\n")
    an.show(3)
    print(4,end="\n")
    an.show(4)
    print(5,end="\n")
    an.show(5)
    print(6,end="\n")
    an.show(6)
    print(7,end="\n")
    an.show(7)
    print(8,end="\n")
    an.show(8)
    print(9,end="\n")
    an.show(9)

