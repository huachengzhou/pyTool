# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout


class MyWindow(QWidget):

    def __init__(self,parent=None):
        super().__init__()
        if parent != None:
            self.setParent(parent)
        self.setWindowTitle("网格布局")
        layout = QGridLayout()
        self.setLayout(layout)
        self.setGeometry(100,100,400,400)
        self.setupUi(layout)
        self.show()
        pass
    def setupUi(self,layout):
        # 准备数据
        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"]
        }
        # 循环创建追加进去
        for x in range(1,10):
            for y in range(1,5):
                btn = QPushButton("-".join([str(x),str(y)]))
                layout.addWidget(btn, x, y)
                pass
        pass


if __name__ == '__main__':
    app = QApplication([])
    my = MyWindow()
    sysUtils.exit(app.exec())