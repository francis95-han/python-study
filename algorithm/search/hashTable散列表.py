#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
如果一个散列函数可以将每一个数据项都映射到不同的槽中，那么
这样的散列函数叫做完美散列函数
'''
# 基本思想
# list=['']*11
# def sanlie(num):
#     a = num % 11
#     list[a] = num
# arr = [12, 123, 412, 127, 1231, 223]
# for i in range(len(arr)):
#     sanlie(arr[i])
# print(list)
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
# +1”的线性探测，
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key,data)

if __name__ == '__main__':
    h=HashTable()
    h[54] = 'cat'
    h[11]='dog'
    h[213]='duck'
    print(h.slots)
    print(h.data)
    h[54]='www'
    print(h.slots)
    print(h.data)