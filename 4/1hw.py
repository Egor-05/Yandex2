import sys


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(375, 200, 375, 200)
        self.setWindowTitle('Арифмометр')

        self.btn = QPushButton('+', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(72, 40)
        self.btn.resize(30, 30)
        self.btn.clicked.connect(self.plus)

        self.btn = QPushButton('-', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(104, 40)
        self.btn.resize(30, 30)
        self.btn.clicked.connect(self.minus)

        self.btn = QPushButton('*', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(136, 40)
        self.btn.resize(30, 30)
        self.btn.clicked.connect(self.multiply)

        self.num1 = QLineEdit(self)
        self.num1.move(20, 40)
        self.num1.resize(50, 30)

        self.num2 = QLineEdit(self)
        self.num2.move(168, 40)
        self.num2.resize(50, 30)

        self.label2 = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label2.setText("=")
        self.label2.move(224, 48)

        self.res = QLineEdit(self)
        self.res.move(236, 40)
        self.res.resize(50, 30)

    def plus(self):
        a = int(self.num1.text())
        b = int(self.num2.text())
        self.res.setText(str(a + b))

    def minus(self):
        a = int(self.num1.text())
        b = int(self.num2.text())
        self.res.setText(str(a - b))

    def multiply(self):
        a = int(self.num1.text())
        b = int(self.num2.text())
        self.res.setText(str(a * b))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())