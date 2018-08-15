#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

top = Tk()


def resize(ev=None):
    label.config(font='Helvetica - %d bold' % scale.get())


# 文本
label = Label(top, text='hello world', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)
# 按钮
button = Button(top, text='close this program', command=top.quit, bg='red', fg="white")
button.pack(fill=X, expand=1)
# 进度条
scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

mainloop()
