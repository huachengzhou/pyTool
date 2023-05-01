import sys as sysUtils
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QSplitter
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
        hSplitter = QSplitter(self)
        vBox = QVBoxLayout(self)
        vBox.addWidget(hSplitter)
        self.setLayout(vBox)
        # 水平线分割
        hSplitter.setOrientation(Qt.Horizontal)
        aFrame = QTextEdit()
        bFrame = QTextEdit()
        aFrame.setPlainText("a")
        bFrame.setPlainText("b")

        hSplitter.addWidget(aFrame)
        hSplitter.addWidget(bFrame)
        hSplitter.setStretchFactor(1,2)

        pass


if __name__ == '__main__':
    app = QApplication([])
    myW = MyWindow("分割器学习")
    sysUtils.exit(app.exec_())