#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
myscreen = curses.initscr()
myscreen.border(0)
myscreen.addstr(12, 25, "Python curses in action!")
myscreen.refresh()
myscreen.getch()