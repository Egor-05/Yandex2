import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
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

        self.btn = QPushButton(self)
        self.btn.setText('Нажми меня')
        self.btn.resize(100, 50)
        self.btn.move(200, 225)

    def mouseMoveEvent(self, event):
        self.x, self.y = event.x(), event.y()
        if self.btn.x() + 110 == x or self.btn - 10 == x:
            print(self.btn.x())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())