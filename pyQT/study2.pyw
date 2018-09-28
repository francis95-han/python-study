#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQT5 学习
"""

import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)
try:
    due = QTime.currentTime()
    message = "Alert"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mnis = sys.argv[1].split(":")
    due = QTime(int(hours), int(mnis))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = "".join(sys.argv[2:])
except ValueError:
    message = "Usage : alert.pyw HH:MM [option message]"
while QTime.currentTime() < due:
    time.sleep(20)
label = QLabel("<font size=10><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
app.exec_()
