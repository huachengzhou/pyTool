import sys as sysUtils
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QDesktopWidget, QMessageBox,QVBoxLayout,QWidget,QPushButton,QHBoxLayout
from PyQt5 import QtCore
from qt_material import apply_stylesheet
from uiqt import MyFILE_UI, MyFORMAT_UI, MyOFFICE_UI
from params import BaseConstant


class MyWindow(QMainWindow):
    typeCount = 0

    # 窗口关闭按钮事件
    def closeEvent(self, event):
        """Shuts down application on close."""
        reply = QMessageBox.question(self, '警告', '<font color=red><b>窗口关闭后，将终止本次运行</b></font>',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 设置参数
    def settingMaximiz(self, num):
        if num < 1:
            available = self.desk.availableGeometry()
            center_pointer = available.center()
            BaseConstant.paramWidth = int(available.width() * BaseConstant.paramW1)
            BaseConstant.paramHeight = int(available.height() * BaseConstant.paramH1)
            rect = QtCore.QRect(int(center_pointer.x() - center_pointer.x() * BaseConstant.paramX1),
                                int(center_pointer.y() - center_pointer.y() * BaseConstant.paramY1),
                                BaseConstant.paramWidth,
                                BaseConstant.paramHeight)
            self.aFrame.setGeometry(BaseConstant.paramX, BaseConstant.paramY-50, BaseConstant.paramWidth,
                                    BaseConstant.paramHeight / 10)
            self.bFrame.setGeometry(BaseConstant.paramX, BaseConstant.paramY + BaseConstant.paramHeight / 10 + 10-70,
                                    BaseConstant.paramWidth, BaseConstant.paramHeight - 80)
            self.stackedLayout.setGeometry(rect)
        else:
            available = self.desk.availableGeometry()
            center_pointer = available.center()
            BaseConstant.paramWidth = int(available.width() * BaseConstant.paramW2)
            BaseConstant.paramHeight = int(available.height() * BaseConstant.paramH2)
            rect = QtCore.QRect(int(center_pointer.x() - center_pointer.x() * BaseConstant.paramX2),
                                int(center_pointer.y() - center_pointer.y() * BaseConstant.paramY2),
                                BaseConstant.paramWidth,
                                BaseConstant.paramHeight)
            self.aFrame.setGeometry(BaseConstant.paramX, BaseConstant.paramY-50, BaseConstant.paramWidth,
                                    BaseConstant.paramHeight / 10)
            self.bFrame.setGeometry(BaseConstant.paramX, BaseConstant.paramY + BaseConstant.paramHeight / 10 -70,
                                    BaseConstant.paramWidth, BaseConstant.paramHeight-90)
            self.stackedLayout.setGeometry(rect)
        pass

    # main 窗口事件
    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                typeCount = -1
                print("窗口最小化")
            elif self.isMaximized():
                self.settingMaximiz(1)
                typeCount = 1
                print("窗口最大化")
            elif self.isFullScreen():
                self.settingMaximiz(2)
                typeCount = 2
                print("全屏显示")
            elif self.isActiveWindow():
                self.settingMaximiz(-1)
                typeCount = 1
                print("活动窗口")

    def __init__(self, title, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle(title)
        desk = QDesktopWidget()
        # 将 QDesktopWidget挂到实例对象上
        self.desk = desk
        # 设置菜单
        self.setupMean()
        # 设置ui
        self.setupUi(desk)
        # self.resize(370, 250)
        # self.setGeometry(200, 200, 500, 400)
        available = desk.availableGeometry()
        center_pointer = available.center()
        self.setGeometry(int(center_pointer.x() - center_pointer.x() * 0.7),
                         int(center_pointer.y() - center_pointer.y() * 0.7),
                         int(available.width() * 0.7),
                         int(available.height() * 0.7))
        self.show()

    def setupUi(self, desk):
        available = desk.availableGeometry()
        center_pointer = available.center()

        BaseConstant.paramWidth = int(available.width() * BaseConstant.paramW1)
        BaseConstant.paramHeight = int(available.height() * BaseConstant.paramH1)
        BaseConstant.paramX = int(center_pointer.x() - center_pointer.x() * 1.0)
        BaseConstant.paramY = int(center_pointer.y() - center_pointer.y() * 0.9)

        aFrame = QWidget(self)
        bFrame = QWidget(self)
        # aFrame.setStyleSheet("background-color:red;")
        # bFrame.setStyleSheet("background-color:blue;")
        # aFrame.setGeometry(BaseConstant.paramX, BaseConstant.paramY - 50, BaseConstant.paramWidth, BaseConstant.paramHeight / 10)
        # bFrame.setGeometry(BaseConstant.paramX, BaseConstant.paramY + BaseConstant.paramHeight / 10 + -60, BaseConstant.paramWidth, BaseConstant.paramHeight - 80)
        aFrame.setGeometry(BaseConstant.paramX,BaseConstant.paramY-50,BaseConstant.paramWidth,BaseConstant.paramHeight/10)
        bFrame.setGeometry(BaseConstant.paramX,BaseConstant.paramY+BaseConstant.paramHeight/10+10-50,BaseConstant.paramWidth,BaseConstant.paramHeight-50)

        hBox = QHBoxLayout()

        btn1 = QPushButton("格式化操作")
        btn1.setObjectName("0")

        btn2 = QPushButton("文件")
        btn2.setObjectName("1")

        btn3 = QPushButton("表格处理")
        btn3.setObjectName("2")

        btn1.clicked.connect(lambda x: self.changeMenuEvent(btn1.objectName(),int(btn1.objectName())))
        btn2.clicked.connect(lambda x: self.changeMenuEvent(btn2.objectName(),int(btn2.objectName())))
        btn3.clicked.connect(lambda x: self.changeMenuEvent(btn3.objectName(),int(btn3.objectName())))

        hBox.addWidget(btn1)
        hBox.addStretch(2)
        hBox.addWidget(btn2)
        hBox.addStretch(2)
        hBox.addWidget(btn3)
        hBox.addStretch(2)

        aFrame.setLayout(hBox)

        layout = QVBoxLayout()

        layout.addWidget(aFrame)
        layout.addWidget(bFrame)

        stackedLayout = QStackedLayout()
        self.stackedLayout = stackedLayout
        self.aFrame = aFrame
        self.bFrame = bFrame
        # 创建单独的Widget
        int_a = stackedLayout.addWidget(MyFILE_UI.MyWindow(bFrame,width=BaseConstant.paramWidth,height=BaseConstant.paramHeight-50,x=BaseConstant.paramX,y=BaseConstant.paramY))
        int_b = stackedLayout.addWidget(MyFORMAT_UI.MyWindow(bFrame,width=BaseConstant.paramWidth,height=BaseConstant.paramHeight-50,x=BaseConstant.paramX,y=BaseConstant.paramY))
        int_c = stackedLayout.addWidget(MyOFFICE_UI.MyWindow(bFrame,width=BaseConstant.paramWidth,height=BaseConstant.paramHeight-50,x=BaseConstant.paramX,y=BaseConstant.paramY))
        stackedLayout.setCurrentIndex(1)

        rect = QtCore.QRect(BaseConstant.paramX,
                            BaseConstant.paramY,
                            BaseConstant.paramWidth,
                            BaseConstant.paramHeight)
        stackedLayout.setGeometry(rect)
        bFrame.setLayout(stackedLayout)

        self.setLayout(layout)
        return [int_a, int_b, int_c]

    def setupMean(self):
        menubar = self.menuBar()



    def changeMenuEvent(self, state, currentIndex):
        if MyWindow.typeCount == 1:
            self.settingMaximiz(1)
            pass
        else:
            self.settingMaximiz(-1)
            pass
        self.stackedLayout.setCurrentIndex(currentIndex)
        print("changeMenuEvent", state)


    pass


if __name__ == '__main__':
    print(sysUtils.argv)
    app = QApplication([])
    extra = {

        # Button colors
        'danger': '#dc3545',
        'warning': '#ffc107',
        'success': '#17a2b8',

        # Font
        'font_family': '微软雅黑',
        'font_size': '13px',
        'line_height': '13px',

        # Density Scale
        'density_scale': '0',

        # environ
        'pyside6': True,
        'linux': True,
    }
    # setup stylesheet
    '''
   'dark_amber.xml',
 'dark_blue.xml',
 'dark_cyan.xml',
 'dark_lightgreen.xml',
 'dark_pink.xml',
 'dark_purple.xml',
 'dark_red.xml',
 'dark_teal.xml',
 'dark_yellow.xml',
 'light_amber.xml',
 'light_blue.xml',
 'light_cyan.xml',
 'light_cyan_500.xml',
 'light_lightgreen.xml',
 'light_pink.xml',
 'light_purple.xml',
 'light_red.xml',
 'light_teal.xml',
 'light_yellow.xml'
    '''
    apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True, extra=extra)
    myW = MyWindow("我的应用")
    sysUtils.exit(app.exec_())
