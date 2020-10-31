# import sys
#
# from PyQt5.QtWidgets import QWidget, QApplication
# from PyQt5.QtCore import Qt
from random import randint
# from PyQt5.QtGui import QPainter, QColor
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.flag = True
#
#     def initUI(self):
#         self.setGeometry(500, 500, 500, 500)
#         self.setWindowTitle('Координаты')
#
#
#
#
#
#     def mousePressEvent(self, event):
#         qp = QPainter()
#         qp.setPen(QColor(0, 255, 0))
#         qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
#         side = randint(25, 50) // 2
#         x, y = event.x(), event.y()
#         x1, y1, x2, y2 = x - side, y - side, x + side, y + side
#         if event.button() == Qt.LeftButton:
#             self.repaint()
#             self.paint.begin(self)
#             qp.drawRect(x1, y1, x2, y2)
#             self.paint.end()
#             self.update()
#             print("Key pressed")
#         elif event.button() == Qt.RightButton:
#             self.repaint()
#             self.paint.begin(self)
#             qp.drawEllipse(x1, y1, x2, y2)
#             self.paint.end()
#             self.update()
#             print("Key pressed")
#
#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Space:
#             print("Key pressed")
#             self.repaint()
#             self.paint.begin(self)
#             qp = QPainter()
#             qp.setPen(QColor(0, 255, 0))
#             qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
#             side = randint(25, 50)
#             side1 = side // 2
#             x1, x2, x3 = self.x - side1, self.x + side1, self.x
#             y1, y2, y3 = self.y - side1, self.y - side1, self.y + side1
#             qp.drawPolygon((x1, y1, x2, y2, x3, y3))
#             self.update()
#             self.paint.end()
#
#     def draw_(self, paint):
#         paint.drawEllipse(self.x, self.y, 10, 10)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec())


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QMouseEvent
from PyQt5.QtCore import Qt, QPoint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.rflag = False
        self.lflag = False
        self.space = False
        self.initUI()

    def initUI(self):
        self.resize(500, 500)
        self.show()
        self.setMouseTracking(True)

    def paintEvent(self, e):
        self.paint = QPainter()
        self.paint.begin(self)
        side = randint(25, 75)
        side1 = side // 2
        if self.rflag:
            self.rflag = False
            self.paint.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.paint.drawRect(self.x - side1, self.y - side1, side, side)
        if self.lflag:
            self.lflag = False
            self.paint.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.paint.drawEllipse(self.x - side1, self.y - side1, side, side)
        if self.space:
            self.space = False
            self.paint.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x1, x2, x3 = QPoint(self.x + side1, self.y + side1), QPoint(self.x - side1, self.y + side1), QPoint(self.x, self.y - side1)
            self.paint.drawPolygon(x3, x2, x1)
        self.paint.end()

    def mouseMoveEvent(self, event):
        self.x, self.y = event.x(), event.y()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.lflag = True
            self.x = e.pos().x()
            self.y = e.pos().y()
            self.update()
        elif e.button() == Qt.RightButton:
            self.rflag = True
            self.x = e.pos().x()
            self.y = e.pos().y()
            self.update()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space:
            self.space = True
            self.update()


app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())