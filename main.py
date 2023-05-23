from Clock import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from ntp import *
from Clock import Clock
from digital import Digital
from weather import get_weathers

# 定义一个名为main_win的类，继承自QWidget类
class main_win(QWidget):
# 定义setupUi函数
    def setupUi(self):
        self.setWindowTitle("course8 by Ryan")
        self.setWindowIcon(QIcon('img/kagami.png'))
        # 设置窗口大小为800x500
        self.resize(800, 500)
        # 创建一行文本框以及按钮控件，并绑定点击事件与回车事件
        self.query = QLineEdit(self)
        self.query.setGeometry(QtCore.QRect(580, 220, 100, 30))
        self.query.setObjectName('query')
        self.query.setText('杭州')
        self.query.returnPressed.connect(self.refresh)
        self.button = QPushButton(self)
        self.button.setGeometry(QtCore.QRect(580, 260, 100, 30))
        self.button.setObjectName('button')
        self.button.setText('查询')
        self.button.clicked.connect(self.refresh)
        # 创建一个表格
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(15, 330, 771, 142))
        self.tableWidget.setObjectName("tableWidget")
        # 设置表格列数为6
        self.tableWidget.setColumnCount(6)
        # 设置表格行数为0
        self.tableWidget.setRowCount(0)
        # 设置字体
        item = QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        # 连接表格选中项改变事件到set_image函数
        self.tableWidget.currentItemChanged.connect(self.set_image)
        # 设置表格为只读
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # 创建一个标签，用来显示天气图像
        self.label = QLabel(self)
        # 设置标签控件的位置和大小
        self.label.setGeometry(QtCore.QRect(20, 20, 300, 251))
        # 设置标签控件显示的文本
        self.label.setText("")
        # 设置标签控件的名称
        self.label.setObjectName("label")
        # 调用retranslateUi方法设置UI的文本信息
        self.retranslateUi(self)
        # 使用QtCore.QMetaObject.connectSlotsByName方法连接UI中的控件和槽函数
        QtCore.QMetaObject.connectSlotsByName(self)

    # 定义retranslateUi方法，用于更新UI的文本信息
    def retranslateUi(self, Widget):
        # 创建一个Qt翻译对象
        _translate = QtCore.QCoreApplication.translate
        # 设置表格控件的列标题文本
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Widget", "日期"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Widget", "天气"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Widget", "风向"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Widget", "最高温度"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Widget", "最低温度"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Widget", "风速"))
        # 设置表格控件的行数
        form.tableWidget.setRowCount(3)

    def set_image(self):
        # 获取当前选中的行号
        row = self.tableWidget.currentRow()
        # 如果当前行号小于 0，则将其设置为 0
        if row < 0:
            row = 0
        img_id = ""
        print(row)
        # 根据当前行对应的天气情况，选择对应的图片名称
        if self.tableWidget.item(row, 1).text() == "阴":
            img_id = "102.png"
        elif self.tableWidget.item(row, 1).text() == "多云":
            img_id = "104.png"
        elif self.tableWidget.item(row, 1).text() == "晴":
            img_id = "100.png"
        elif self.tableWidget.item(row, 1).text().__contains__("雨"):
            img_id = "306.png"
        elif self.tableWidget.item(row, 1).text().__contains__("雪"):
            img_id = "401.png"
        # 通过图片名称加载对应的图片，并将其设置为 label 的 pixmap
        self.pixmap = QPixmap("img/" + img_id)
        self.label.setPixmap(self.pixmap)

# 定义refresh()方法, 用于刷新表格中的内容
    def refresh(self):
        # 得到要查询的城市编码
        city_code = self.query.text()
        # 得到该城市近三天的天气情况
        weathers = get_weathers(city_code)
        print(weathers.city_name)
        for i in range(0, 3):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(''.join(weathers.city_weather_list[i].date)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(''.join(weathers.city_weather_list[i].text_day)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(''.join(weathers.city_weather_list[i].wind_direction)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(''.join(weathers.city_weather_list[i].high)))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(''.join(weathers.city_weather_list[i].low)))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(''.join(weathers.city_weather_list[i].wind_speed)))
        # 调用set_image()方法，根据表格中选中的天气情况，在界面上显示对应的天气图片。
        self.set_image()

if __name__ == "__main__":
    # 该部分代码用于获取网络时间，这里使用了ntp模块，如果出现错误，则跳过这一步
    try:
        ntp.ntp()
    except:
        pass
    app = QApplication(sys.argv)
    # 创建一个Qt应用程序和main_win类的实例对象，并调用setupUi()方法，创建GUI界面。
    form = main_win()
    form.setupUi()
    form_clock = Clock()
    form_clock.setParent(form)
    form_clock.setGeometry(270, 40, 200, 200)
    form_clock.show()
    form_digital = Digital()
    form_digital.setParent(form)
    form_digital.setGeometry(510, 40, 250, 150)
    # 创建时钟和数字时钟的实例对象，并设置它们的父级为form，设置位置和大小，最后显示出来。
    form_digital.show()
    form.show()
    form.refresh()
    # 显示GUI界面，并调用refresh()方法，启动Qt应用程序的事件循环，等待用户的操作。
    app.exec_()