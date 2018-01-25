#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import partial

import Tkinter

root = Tkinter.Tk()
myButton = partial(Tkinter.Button, root, fg="white", bg="blue")
b1 = myButton(text="Button1")
b2 = myButton(text="Button2")
qb = myButton(text='QUIT', bg='red', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PEAs')
root.mainloop()
