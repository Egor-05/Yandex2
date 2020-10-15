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
        self.setGeometry(640, 640, 640, 640)
        self.setWindowTitle('Арифмометр')

        self.btn = QPushButton('Показать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 76)
        self.btn.resize(100, 30)
        self.btn.clicked.connect(self.draw)

        self.inp1 = QLineEdit(self)
        self.inp1.move(350, 26)
        self.inp1.resize(130, 30)

        self.inp2 = QLineEdit(self)
        self.inp2.move(350, 76)
        self.inp2.resize(130, 30)

        self.inp3 = QLineEdit(self)
        self.inp3.move(350, 126)
        self.inp3.resize(130, 30)

        self.label = QLabel(self)
        self.label.setText("side")
        self.label.move(300, 30)

        self.label = QLabel(self)
        self.label.setText("coeff")
        self.label.move(300, 80)

        self.label = QLabel(self)
        self.label.setText("n")
        self.label.move(300, 130)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        if self.inp3.text() != '':
            qp.setBrush(QColor(255, 255, 255))
            side = int(self.inp1.text())
            for i in range(int(self.inp3.text())):
                x1 = (510 / 2) - side / 2
                y1 = (510 / 2 + 130) - side / 2
                x2 = x1 + side
                y2 = y1 + side
                qp.drawRect(x1, y1, x2, y2)
                side *= float(self.inp2.text())


    def draw(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())