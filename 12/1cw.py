import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Координаты')

        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.x, self.y = event.x(), event.y()

    def mousePressEvent(self, event):
        qp = QPainter()
        qp.setPen(QColor(0, 255, 0))
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        side = randint(25, 50) // 2
        x, y = event.x(), event.y()
        x1, y1, x2, y2 = x - side, y - side, x + side, y + side
        if event.button() == Qt.LeftButton:
            self.repaint()
            qp.drawRect(x1, y1, x2, y2)
            self.update()
            print("Key pressed")
        elif event.button() == Qt.RightButton:
            self.repaint()
            qp.drawEllipse(x1, y1, x2, y2)
            self.update()
            print("Key pressed")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space:
            print("Key pressed")
            self.repaint()
            qp = QPainter()
            qp.setPen(QColor(0, 255, 0))
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            side = randint(25, 50)
            side1 = side // 2
            x1, x2, x3 = self.x - side1, self.x + side1, self.x
            y1, y2, y3 = self.y - side1, self.y - side1, self.y + side1
            qp.drawPolygon((x1, y1, x2, y2, x3, y3))
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())