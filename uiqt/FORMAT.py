import sys as sysUtils
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QSplitter, QPushButton,QMessageBox
from PyQt5.QtCore import Qt
import re as reUtils


class MyWindow(QWidget):

    def __init__(self, parent=None, title=""):
        super().__init__()
        if parent != None:
            self.setParent(parent)
        self.setWindowTitle(title)
        self.setupUi()
        self.setGeometry(100, 100, 400, 400)
        self.show()

    def setupUi(self):
        hSplitter = QSplitter(self)
        vBox = QVBoxLayout(self)
        vBox.addWidget(hSplitter)
        self.setLayout(vBox)
        # 水平线分割
        hSplitter.setOrientation(Qt.Vertical)
        codeMirror = QTextEdit()
        self.codeMirror = codeMirror
        bFrame = QWidget()
        bFrame.setParent(hSplitter)
        bQHBoxLayout = QHBoxLayout(hSplitter)
        bFrame.setLayout(bQHBoxLayout)
        codeMirrorResult = QTextEdit()
        self.codeMirrorResult = codeMirrorResult
        codeMirror.setPlainText("")
        codeMirrorResult.setPlainText("")
        self.setupCenter(bQHBoxLayout)

        hSplitter.addWidget(codeMirror)
        hSplitter.setStretchFactor(2, 1)
        hSplitter.addWidget(bFrame)
        hSplitter.setStretchFactor(1, 1)
        hSplitter.addWidget(codeMirrorResult)
        hSplitter.setStretchFactor(2, 1)

        pass

    def setupCenter(self, bQHBoxLayout):
        btn1 = QPushButton("驼峰转下划线")
        btn2 = QPushButton("下划线转驼峰")
        btn3 = QPushButton("清空结果")

        btn3.clicked.connect(self.clearQTextEdit)
        btn1.clicked.connect(self.camel_to_snake)
        btn2.clicked.connect(self.to_lower_camel)

        bQHBoxLayout.addWidget(btn1)
        # bQHBoxLayout.addStretch(1)
        bQHBoxLayout.addWidget(btn2)
        # bQHBoxLayout.addStretch(1)
        bQHBoxLayout.addWidget(btn3)

    # 清除 文本框
    def clearQTextEdit(self):
        self.codeMirror.setPlainText("")
        self.codeMirrorResult.setPlainText("")
        pass

    # 转换驼峰命名 为下划线命名
    def camel_to_snake(self):
        name = self.codeMirror.toPlainText()
        if len(name) == 0 or len(name) == 0:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '没有输入字符串')
            msg_box.exec_()
        else:
            name = reUtils.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
            str1 = reUtils.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
            self.codeMirrorResult.setPlainText(str1)
    def to_lower_camel(self):
        """下划线转小驼峰法命名"""
        name = self.codeMirror.toPlainText()
        if len(name) == 0 or len(name) == 0:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '没有输入字符串')
            msg_box.exec_()
        else:
            str1 = reUtils.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), name.lower())
            self.codeMirrorResult.setPlainText(str1)


if __name__ == '__main__':
    app = QApplication([])
    myW = MyWindow("分割器学习")
    sysUtils.exit(app.exec_())
