import sys


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.Qt import *


class Example(QWidget):
    btns = []

    num1 = ''
    num2 = ''
    znak = ''

    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(290, 420, 290, 420)
        self.setWindowTitle('Калькулятор')

        x = -60
        y = 6
        for j in range(1, 10):
            x = -60 if j % 3 == 1 else x
            if j % 3 == 1:
                y += 70
            x += 70
            self.btns.append(QPushButton(self))
            self.btns[j - 1].setText(str(j))
            self.btns[j - 1].resize(61, 61)
            self.btns[j - 1].move(x, y)
            self.btns[j - 1].clicked.connect(self.pressed_num)

        self.btn0 = QPushButton(self)
        self.btn0.setText('0')
        self.btn0.resize(61, 61)
        self.btn0.move(80, 286)
        self.btn0.clicked.connect(self.pressed_num)

        self.btn_plus = QPushButton(self)
        self.btn_plus.setText('+')
        self.btn_plus.resize(61, 61)
        self.btn_plus.move(220, 76)
        self.btn_plus.clicked.connect(self.plus)

        self.btn_minus = QPushButton(self)
        self.btn_minus.setText('-')
        self.btn_minus.resize(61, 61)
        self.btn_minus.move(220, 146)
        self.btn_minus.clicked.connect(self.minus)

        self.btn_delit = QPushButton(self)
        self.btn_delit.setText('/')
        self.btn_delit.resize(61, 61)
        self.btn_delit.move(220, 286)
        self.btn_delit.clicked.connect(self.delit)

        self.btn_multiply = QPushButton(self)
        self.btn_multiply.setText('*')
        self.btn_multiply.resize(61, 61)
        self.btn_multiply.move(220, 216)
        self.btn_multiply.clicked.connect(self.multiply)

        self.btn_flt = QPushButton(self)
        self.btn_flt.setText('.')
        self.btn_flt.resize(61, 61)
        self.btn_flt.move(10, 356)
        self.btn_flt.clicked.connect(self.flt)

        self.btn_count = QPushButton(self)
        self.btn_count.setText('=')
        self.btn_count.resize(131, 61)
        self.btn_count.move(150, 356)
        self.btn_count.clicked.connect(self.count)

        self.btn_pm = QPushButton(self)
        self.btn_pm.setText('±')
        self.btn_pm.resize(61, 61)
        self.btn_pm.move(80, 356)
        self.btn_pm.clicked.connect(self.pm)

        self.btnC = QPushButton(self)
        self.btnC.setText('C')
        self.btnC.resize(61, 61)
        self.btnC.move(10, 286)
        self.btnC.clicked.connect(self.c)

        self.btnCE = QPushButton(self)
        self.btnCE.setText('CE')
        self.btnCE.resize(61, 61)
        self.btnCE.move(150, 286)
        self.btnCE.clicked.connect(self.ce)

        self.res = QLineEdit(self)
        f = self.res.font()
        f.setPointSize(24)
        self.res.setFont(f)
        self.res.setAlignment(Qt.AlignRight)
        self.res.resize(271, 61)
        self.res.move(10, 10)

    def plus(self):
        self.znak = '+'
        self.res.setText('')

    def minus(self):
        self.znak = '-'
        self.res.setText('')

    def multiply(self):
        self.znak = '*'
        self.res.setText('')

    def delit(self):
        self.znak = '/'
        self.res.setText('')

    def flt(self):
        if self.num1 == '':
            self.res.setText('ERROR')
        elif self.num1 != '' and self.num1.count('.') < 1 and self.znak == '':
            self.num1 += '.'
            self.res.setText(self.res.text() + '.')
        elif self.num2 != '' and self.num2.count('.') < 1:
            self.num2 += '.'
            self.res.setText(self.res.text() + '.')

    def count(self):
        if self.znak == '/' and self.num2 == '0':
            self.res.setText('ERROR')
        else:
            self.res.setText(str(eval(self.num1 + self.znak + self.num2)))
        self.num1 = str(eval(self.num1 + self.znak + self.num2))
        self.num2 = self.znak = ''

    def pressed_num(self):
        if self.num1 == '' and self.znak != '':
            self.res.setText('ERROR')
        elif self.znak == '':
            self.num1 += self.sender().text()
        else:
            self.num2 += self.sender().text()
        self.res.setText(self.res.text() + self.sender().text())

    def ce(self):
        self.res.setText('')
        self.num1 = self.num2 = self.znak = ''

    def c(self):
        if self.res.text() == '' and self.znak != '':
            self.znak = ''
            self.res.setText(self.num1)
        elif self.res.text() != '':
            self.res.setText(self.res.text()[:-1])
            if self.znak == '':
                self.num1 = self.num1[:-1]
            else:
                self.num2 = self.num2[:-1]

    def pm(self):
        if self.znak == '':
            self.num1 = str(-int(self.num1))
            self.res.setText(self.num1)
        else:
            self.num2 = str(-int(self.num2))
            self.res.setText(self.num2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())