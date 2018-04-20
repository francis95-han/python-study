#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author zhangbohan.dell@gmail.com
    @function:
    @create 2018/4/18 19:31"""


from pydbg import *
from pydbg.defines import *
# pydbg安装还有问题，现在还不能用   2018.4.18
import struct
import random


def printf_randomizer(dbg):
    parameter_addr = dbg.context.Esp + 0x8
    counter  = dbg.read_process_memory(parameter_addr,4)
    counter  = struct.unpack("L",counter)[0]
    print("Counter: %d" % int(counter))
    random_counter = random.randint(1,100)
    random_counter = struct.pack("L",random_counter)[0]

    dbg.write_process_memory(parameter_addr,random_counter)

    return DBG_CONTINUE


dbg = pydbg()
pid=input("please enter the printf_loop.py  PID:")

dbg.attach(int(pid))


printf_address = dbg.func_resolve("msvcrt","printf")
dbg.bp_set(printf_address,description="printf_adress",handler=printf_randomizer)

dbg.run()

