import sys as sysUtils
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout,QHBoxLayout, QSplitter,QPushButton
from PyQt5.QtCore import Qt

class MyWindow(QWidget):

    def __init__(self,parent=None,title="sdhsdhsd"):
        super().__init__()
        if parent != None:
            self.setParent(parent)
        self.setWindowTitle(title)
        self.setupUi()
        self.setGeometry(100,100,400,400)
        self.show()

    def setupUi(self):
        btn1 = QPushButton("按钮1")

        hSplitter = QSplitter(self)
        vBox = QVBoxLayout(self)
        vBox.addWidget(hSplitter)
        self.setLayout(vBox)
        # 水平线分割
        hSplitter.setOrientation(Qt.Vertical)
        aFrame = QTextEdit()
        bFrame = QWidget()
        bFrame.setParent(hSplitter)
        bQHBoxLayout = QHBoxLayout(hSplitter)
        bFrame.setLayout(bQHBoxLayout)
        cFrame = QTextEdit()
        aFrame.setPlainText("")
        cFrame.setPlainText("")
        self.setupCenter(bQHBoxLayout)

        hSplitter.addWidget(aFrame)
        hSplitter.setStretchFactor(2, 1)
        hSplitter.addWidget(bFrame)
        hSplitter.setStretchFactor(1,1)
        hSplitter.addWidget(cFrame)
        hSplitter.setStretchFactor(2, 1)

        pass
    def setupCenter(self,bQHBoxLayout):
        btn1 = QPushButton("驼峰转下划线")
        btn2 = QPushButton("下划线转驼峰")
        btn3 = QPushButton("清空结果")

        bQHBoxLayout.addWidget(btn1)
        # bQHBoxLayout.addStretch(1)
        bQHBoxLayout.addWidget(btn2)
        # bQHBoxLayout.addStretch(1)
        bQHBoxLayout.addWidget(btn3)


        pass

if __name__ == '__main__':
    app = QApplication([])
    myW = MyWindow("分割器学习")
    sysUtils.exit(app.exec_())