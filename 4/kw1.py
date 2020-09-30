import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(375, 50, 375, 50)
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 10)
        self.btn.clicked.connect(self.hello)


        self.name_input = QLineEdit(self)
        self.name_input.move(40, 10)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(232, 10)

    def hello(self):
        if self.s % 2 == 0:
            message = self.name_input.text()
            self.name_input.clear()
            self.name_input2.setText(message)
            self.btn.setText('<-')
        else:
            message = self.name_input2.text()
            self.name_input2.clear()
            self.name_input.setText(message)
            self.btn.setText('->')
        self.s += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())