#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
pyqt 学习
"""
from __future__ import division

import sys
from math import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Example(QDialog):

    def __init__(self,parent =None):
        super(Example,self).__init__(parent)
        self.lineEdit = QLineEdit("Type an expression and press enter")
        self.browser = QTextBrowser()
        self.initUI()

    def initUI(self):
        self.lineEdit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        self.lineEdit.setFocus()
        self.lineEdit.textChanged.connect(self.browser.setText)
        self.setWindowTitle("Calculate")
        self.resize(600, 400)
        self.show()

    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
