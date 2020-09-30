import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QLineEdit, QPushButton, QLabel
from random import randint


class Example(QWidget):
    num = randint(10, 50)
    moves = 10
    btn1num = randint(1, 10)
    btn2num = randint(-10, -5)

    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(340, 200, 340, 200)
        self.setWindowTitle('Фокус со словами')

        self.mes = QLineEdit(self)
        self.mes.resize(300, 30)
        self.mes.move(20, 20)
        self.mes.setReadOnly(True)

        self.btn1 = QPushButton(str(self.btn1num), self)
        self.btn1.move(20, 60)
        self.btn1.resize(90, 35)
        self.btn1.clicked.connect(self.func)

        self.btn2 = QPushButton(str(self.btn2num), self)
        self.btn2.move(230, 60)
        self.btn2.resize(90, 35)
        self.btn2.clicked.connect(self.func)

        self.label1 = QLabel(self)
        self.label1.setText("Ходов осталось:")
        self.label1.move(20, 120)

        self.label2 = QLabel(self)
        self.label2.setText("Текущее число:")
        self.label2.move(20, 160)

        self.move = QLCDNumber(self)
        self.move.resize(100, 30)
        self.move.move(200, 113)
        self.move.display(self.moves)

        self.numb = QLCDNumber(self)
        self.numb.resize(100, 30)
        self.numb.move(200, 153)
        self.numb.display(self.num)

    def func(self):
        a = int(self.sender().text())
        self.num += a
        self.moves -= 1
        end = False
        self.numb.display(self.num)
        self.move.display(self.moves)
        if self.num == 0:
            self.mes.setText('Вы выиграли!')
            end = True
        elif self.moves == 0:
            self.mes.setText('Вы проиграли!')
            end = True
        if end:
            self.num = randint(10, 50)
            self.moves = 10
            self.btn1num = randint(1, 10)
            self.btn2num = randint(-10, -1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())