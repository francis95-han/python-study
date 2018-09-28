#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
pyqt demo
"""

import sys
from PyQt5.QtGui import QFont    
from PyQt5.QtWidgets import *

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        title = QLabel('<font coloe=red size=12>请选择您要转化的文件</font>')
        chooseFiles = QPushButton("选择文件")
        chooseFiles.clicked.connect(self.openFile)
        files =QTextEdit()
        files.resize(500,100)
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,1)
        grid.addWidget(chooseFiles,2,2)
        grid.addWidget(files,3,1,5,1)
        self.setLayout(grid) 
        self.resize(600, 400)
        self.setWindowTitle('Tooltips')    
        self.show()

      

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
            
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())