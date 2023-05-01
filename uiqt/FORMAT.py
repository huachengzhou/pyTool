# -*- coding: utf-8 -*-


import sys as sysUtils
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PyQt5.QtGui import QIcon,  QFont
import random as randomUtils
from PyQt5.QtCore import Qt


class MyWindow(QWidget):

    def __init__(self,parent=None):
        super().__init__()
        if parent != None:
            self.setParent(parent)
        desk = QDesktopWidget()
        available = desk.availableGeometry()
        center_pointer = available.center()

        # self.setGeometry(center_pointer.x() - 300, center_pointer.y() - 200, available.width() / 2,
        #                  available.height() / 2)
        self.setGeometry(int(center_pointer.x() - center_pointer.x() * 0.7),
                         int(center_pointer.y() - center_pointer.y() * 0.7),
                         int(available.width() * 0.7),
                         int(available.height() * 0.7))

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)

        # 因为这里没有添加任何空白占位控件，所以已有的这些控件将会将这个横向布局给占满。本来这些控件按默认长度来排列的话会占不满整个长度，但因为没有空白占位控件，所以QT会自动将这些控件按它自己的规则比例来拉升填满

        # layout.addStretch(0)
        # layout.setSpacing(0)
        self.setLayout(layout)
        self.setupUI(layout)
        self.show()

    def setupUI(self, layout):
        self.setWindowTitle("复杂表格学习")
        self.setWindowIcon(QIcon("free.png"))

        table = QTableWidget()
        layout.addWidget(table)
        # table.setParent(self)
        #  构造宽度为 width、高度为 height 的 QSize  对象
        # table.setBaseSize(500, 500)
        #  x, y , w, h
        table.setGeometry(10, 10, 500, 1600)

        # 隐藏水平表头
        # table.horizontalHeader().hide()
        # 隐藏垂直表头
        # table.verticalHeader().hide()

        # 随窗口大小自动调整行高
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置 表格 行的数量
        table.setRowCount(100)
        # 设置表格 列的数量
        table.setColumnCount(int(randomUtils.randrange(15, 20)))

        list1 = []
        for columnIndex in range(1, table.columnCount() + 1):
            list1.append(str(columnIndex) + "列")
            pass
        table.setHorizontalHeaderLabels(list1)

        list2 = []
        for rowIndex in range(1, table.rowCount() + 1):
            list2.append(str(rowIndex) + "行")
            pass
        table.setVerticalHeaderLabels(list2)

        font = QFont()  # 实例化字体对象
        font.setFamily('微软雅黑')  # 字体
        font.setBold(False)  # 加粗
        font.setItalic(True)  # 斜体
        font.setStrikeOut(False)  # 删除线
        font.setUnderline(True)  # 下划线
        font.setPointSize(15)  # 字体大小

        for rowIndex in range(1, table.rowCount() + 1):
            for columnIndex in range(1, table.columnCount() + 1):
                item = QTableWidgetItem(str(rowIndex) + "-" + str(columnIndex))
                item.setFont(font)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                table.setItem(rowIndex - 1, columnIndex - 1, item)
                pass
        pass
        table.itemChanged.connect(lambda item_a: print(f"信号槽 值改变:{item_a}"))
        table.itemClicked.connect(lambda item_a: print(f"信号槽 click:{item_a}"))
        table.itemDoubleClicked.connect(lambda item_a: print(f"信号槽 DoubleClick:{item_a}"))


if __name__ == '__main__':
    app = QApplication(sysUtils.argv)
    my = MyWindow()

    sysUtils.exit(app.exec_())
