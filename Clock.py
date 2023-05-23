from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from math import *
class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("course8 by Ryan")
        self.setWindowIcon(QIcon('img/kagami.png'))
        self.timer = QTimer()
        # 设置窗口计时器
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def paintEvent(self, event):

        # 画出时分秒三个指针的形状

        hour_point = [QPoint(2, 8), QPoint(-2, 8), QPoint(0, -40)]
        min_point = [QPoint(3, 8), QPoint(-3, 8), QPoint(0, -70)]
        secn_point = [QPoint(3, 8), QPoint(-3, 8), QPoint(0, -100)]
        # 定义三种颜色、用于后面设置三种指针的颜色
        hour_color = QColor(182, 98, 0, 182)
        min_color = QColor(0, 130, 130, 155)
        sec_color = QColor(0, 155, 227, 155)
        # 获取QWidget对象的宽度和长度的最小值
        min_size = min(self.width(), self.height())
        # 创建坐标系图像绘制对象
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # 将QWidget对象的中心位置作为绘制的中心坐标点
        painter.translate(self.width() / 2, self.height() / 2)
        # 对尺寸进行缩放
        painter.scale(int(min_size / 200), int(min_size / 200))
        # 保存状态
        painter.save()


        # 绘制时钟表盘的时间刻度线
        for a in range(0, 60):
            if (a % 5) != 0:
                # 每1/60绘制一个刻度线作为分钟刻度线
                painter.setPen(min_color)
                painter.drawLine(92, 0, 96, 0)
            else:
                # 每5/60绘制一个刻度线作为小时刻度线
                painter.setPen(hour_color)
                painter.drawLine(88, 0, 96, 0)  # 绘制小时刻度线
            # 每分钟旋转6度
            painter.rotate(360 / 60)
        # 恢复状态
        painter.restore()


        # 绘制时钟表盘上面的数字

        # 保存状态
        painter.save()
        # 获取字体对象
        font = painter.font()
        # 设置粗体
        font.setBold(True)
        painter.setFont(font)
        # 获取字体大小
        font_size = 15
        # 设置之前定义好的颜色
        painter.setPen(hour_color)
        radius = 100
        for i in range(0, 12):
            # 按照12小时制，每三个小时绘制一个小时数字，需要遍历4次
            hour_num = i + 3  # 按QT-Qpainter的坐标系换算，3小时的刻度线对应坐标轴0度
            if hour_num > 12:
                hour_num = hour_num - 12
            # 根据字体的大小计算出写入小时数字的x、y的位置
            x = radius * 0.8 * cos(i * 30 * pi / 180.0) - font_size
            y = radius * 0.8 * sin(i * 30 * pi / 180.0) - font_size / 2.0
            width = font_size * 2
            height = font_size
            painter.drawText(QRectF(x, y, width, height), Qt.AlignCenter, str(hour_num))
        # 恢复状态
        painter.restore()


        # 绘制时钟表盘的时、分、秒的指针

        # 获取当前时间
        time = QTime.currentTime()
        # 绘制小时指针
        painter.save()
        # 取消轮廓线
        painter.setPen(Qt.NoPen)
        # 设置小时指针的颜色
        painter.setBrush(hour_color)
        # 小时指针逆时针旋转
        painter.rotate(30 * (time.hour() + time.minute() / 60))
        # 绘制时钟指针
        painter.drawConvexPolygon(QPolygonF(hour_point))
        # 恢复状态
        painter.restore()
        # 绘制分钟指针
        painter.save()
        # 取消轮廓线
        painter.setPen(Qt.NoPen)
        # 设置分钟指针的颜色
        painter.setBrush(min_color)
        # 分钟指针逆时针旋转
        painter.rotate(6 * (time.minute() + time.second() / 60))
        # 绘制分钟指针
        painter.drawConvexPolygon(QPolygonF(min_point))
        # 恢复状态
        painter.restore()
        # 绘制秒钟指针
        painter.save()
        # 取消轮廓线
        painter.setPen(Qt.NoPen)
        # 设置秒针颜色
        painter.setBrush(sec_color)
        # 秒钟指针逆时针旋转
        painter.rotate(6 * time.second())
        # 绘制秒钟指针
        painter.drawConvexPolygon(QPolygonF(secn_point))
        # 恢复状态
        painter.restore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Clock()
    form.show()
    app.exec_()