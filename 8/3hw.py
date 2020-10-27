import sys


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(510, 640, 510, 640)
        self.setWindowTitle('Арифмометр')

        self.btn = QPushButton('Показать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 60)
        self.btn.resize(100, 30)
        self.btn.clicked.connect(self.draw)

        self.inp2 = QLineEdit(self)
        self.inp2.move(70, 15)
        self.inp2.resize(130, 30)

        self.inp3 = QLineEdit(self)
        self.inp3.move(325, 15)
        self.inp3.resize(130, 30)

        self.label = QLabel(self)
        self.label.setText("coeff")
        self.label.move(20, 20)

        self.label1 = QLabel(self)
        self.label1.setText("n")
        self.label1.move(275, 20)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        if self.inp3.text() != '':
            qp.setPen(QColor(255, 0, 0))
            side = 300
            c = float(self.inp2.text())
            x = (510 - side) // 2
            y = 130 + x
            x1 = x
            x2 = x + side
            y1 = y
            y2 = y + side
            qp.drawLine(x1, y1, x2, y1)
            qp.drawLine(x2, y1, x2, y2)
            qp.drawLine(x1, y2, x2, y2)
            qp.drawLine(x1, y1, x1, y2)
            x12, y12 = self.find_coords(1 - c, x1, y1, x2, y1)
            x22, y22 = self.find_coords(1 - c, x2, y1, x2, y2)
            x32, y32 = self.find_coords(c, x1, y2, x2, y2)
            x42, y42 = self.find_coords(c, x1, y1, x1, y2)
            for i in range(int(self.inp3.text()) - 1):
                side *= c
                x1, y1 = x12, y12
                x2, y2 = x22, y22
                x3, y3 = x32, y32
                x4, y4 = x42, y42
                qp.drawLine(x1, y1, x2, y2)
                qp.drawLine(x2, y2, x3, y3)
                qp.drawLine(x3, y3, x4, y4)
                qp.drawLine(x4, y4, x1, y1)
                x12, y12 = self.find_coords(1 - c, x1, y1, x2, y2)
                x22, y22 = self.find_coords(1 - c, x2, y2, x3, y3)
                x32, y32 = self.find_coords(1 - c, x3, y3, x4, y4)
                x42, y42 = self.find_coords(1 - c, x4, y4, x1, y1)

    def draw(self):
        self.update()

    def find_coords(self, c, x1, y1, x2, y2):
        c2 = 1 - c
        x = (x1 + (c / c2) * x2) / (1 + (c / c2))
        y = (y1 + (c / c2) * y2) / (1 + (c / c2))
        return x, y


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())