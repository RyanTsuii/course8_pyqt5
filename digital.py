import sys
import time
from datetime import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Digital(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("course8 by Ryan")
        self.setWindowIcon(QIcon('img/kagami.png'))
        # 创建 QTimer 对象
        self.timer = QTimer()
        # 绑定 QTimer 的 timeout 信号到 self.update() 方法上
        self.timer.timeout.connect(self.update)
        # 每隔 1000 毫秒启动 QTimer 对象
        self.timer.start(1000)
        # 调用 UI 文件中的 setupUi() 方法初始化窗口部件
        Digital.setupUi(self)

    def update(self):
        # 获取当前时间的时间戳
        now_time_stamp = time.time()
        # 将时间戳转换成日期时间格式
        now_time = datetime.fromtimestamp(now_time_stamp)
        # 将日期格式化为字符串，并在 lcdNumber 控件上显示
        self.lcdNumber1.display(now_time.strftime("%Y-%m-%d"))
        # 将时间格式化为字符串，并在 lcdNumber_2 控件上显示
        self.lcdNumber2.display(now_time.strftime("%H:%M:%S"))



    def setupUi(self):
        # 设置窗口大小为 250 x 150
        self.resize(265,150)
        # 创建 QLCDNumber 控件
        self.lcdNumber1 = QtWidgets.QLCDNumber(self)
        # 设置 QLCDNumber 控件的位置和大小
        self.lcdNumber1.setGeometry(QtCore.QRect(0, 10, 250, 50))
        # 设置 QLCDNumber 控件显示的位数
        self.lcdNumber1.setDigitCount(10)
        # 设置 QLCDNumber 控件的对象名称
        self.lcdNumber1.setObjectName("lcdNumber1")
        # 创建第二个 QLCDNumber 控件
        self.lcdNumber2 = QtWidgets.QLCDNumber(self)
        # 设置第二个 QLCDNumber 控件的位置和大小
        self.lcdNumber2.setGeometry(QtCore.QRect(0, 70, 250, 50))
        # 设置第二个 QLCDNumber 控件显示的位数
        self.lcdNumber2.setDigitCount(8)
        #  设置第二个 QLCDNumber 控件的对象名称
        self.lcdNumber2.setObjectName("lcdNumber_2")
        # 调用 retranslateUi() 方法设置界面文字
        self.retranslateUi(self)
        # 连接对象的槽函数
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate  # 获取翻译函数



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Digital()
    form.show()
    app.exec_()
