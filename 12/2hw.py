import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Координаты')

        self.setMouseTracking(True)

        self.pixmap = QPixmap('nlo.png')
        self.label = QLabel(self)
        self.label.resize(41, 31)
        self.label.setPixmap(self.pixmap)
        self.label.move(100, 100)

    def move_wrap(self, move):
        x = self.label.x()
        y = self.label.y()
        self.label.move(x + move[0], y + move[1])
        if x < 0:
            self.label.move(500, y)
        if x > 500:
            self.label.move(0, y)
        if y < 0:
            self.label.move(x, 500)
        if y > 500:
            self.label.move(x, 0)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.move_wrap((0, -10))
        elif e.key() == Qt.Key_Down:
            self.move_wrap((0, 10))
        elif e.key() == Qt.Key_Right:
            self.move_wrap((10, 0))
        elif e.key() == Qt.Key_Left:
            self.move_wrap((-10, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


