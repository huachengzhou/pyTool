import sys as sysUtils
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QDesktopWidget, QMessageBox, QAction
from PyQt5 import QtCore
from qt_material import apply_stylesheet
from means import MyFILE, MyFORMAT, MyOFFICE
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
            self.stackedLayout.setGeometry(rect)
            print(BaseConstant.paramWidth,BaseConstant.paramHeight)
        else:
            available = self.desk.availableGeometry()
            center_pointer = available.center()
            BaseConstant.paramWidth = int(available.width() * BaseConstant.paramW2)
            BaseConstant.paramHeight = int(available.height() * BaseConstant.paramH2)
            rect = QtCore.QRect(int(center_pointer.x() - center_pointer.x() * BaseConstant.paramX2),
                                int(center_pointer.y() - center_pointer.y() * BaseConstant.paramY2),
                                BaseConstant.paramWidth,
                                BaseConstant.paramHeight)
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
        stackedLayout = QStackedLayout()
        available = desk.availableGeometry()
        center_pointer = available.center()
        self.stackedLayout = stackedLayout

        BaseConstant.paramWidth = int(available.width() * BaseConstant.paramW1)
        BaseConstant.paramHeight = int(available.height() * BaseConstant.paramH1)
        BaseConstant.paramX = int(center_pointer.x() - center_pointer.x() * 1.0)
        BaseConstant.paramY = int(center_pointer.y() - center_pointer.y() * 0.9)

        # 创建单独的Widget
        int_a = stackedLayout.addWidget(MyFILE_UI.MyWindow(self,width=BaseConstant.paramWidth,height=BaseConstant.paramHeight,x=BaseConstant.paramX,y=BaseConstant.paramY))
        int_b = stackedLayout.addWidget(MyFORMAT_UI.MyWindow(self,width=BaseConstant.paramWidth,height=BaseConstant.paramHeight,x=BaseConstant.paramX,y=BaseConstant.paramY))
        int_c = stackedLayout.addWidget(MyOFFICE_UI.MyWindow(self,width=BaseConstant.paramWidth,height=BaseConstant.paramHeight,x=BaseConstant.paramX,y=BaseConstant.paramY))

        stackedLayout.setCurrentIndex(1)
        print(int_a, int_b, int_c)

        rect = QtCore.QRect(BaseConstant.paramX,
                            BaseConstant.paramY,
                            BaseConstant.paramWidth,
                            BaseConstant.paramHeight)
        stackedLayout.setGeometry(rect)
        self.setLayout(stackedLayout)
        return [int_a, int_b, int_c]

    def setupMean(self):
        menubar = self.menuBar()

        meanA = MyFILE.toMean(self)
        meanA.triggered.connect(lambda checked: self.changeMenuEvent(checked, 0))
        menubar.addMenu(meanA)

        meanB = MyFORMAT.toMean(self)
        meanB.triggered.connect(lambda checked: self.changeMenuEvent(checked, 1))
        menubar.addMenu(meanB)

        meanC = MyOFFICE.toMean(self)
        meanC.triggered.connect(lambda checked: self.changeMenuEvent(checked, 2))
        menubar.addMenu(meanC)

        print(meanA, meanB, meanC)

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
