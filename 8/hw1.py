import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Выберите кол-во цветов', self)
        self.btn.move(0, 0)
        self.do_paint = False
        self.btn.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def run(self):
        country, ok_pressed = QInputDialog.getItem(
            self, "", "Выберите количество цветов",
            ("1", "2", "3", "4"), 1, False)
        if ok_pressed:
            self.a = country
            self.paint()

    def draw_flag(self, qp):
        for i in range(int(self.a)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawRect(30, 30 * (i + 1), 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())