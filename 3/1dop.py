import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(375, 50, 375, 50)
        self.setWindowTitle('Шестая программа')

        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 10)
        self.btn.clicked.connect(self.hello)


        # self.name_input = QLineEdit(self)
        # self.name_input.move(40, 10)

        self.name_input2 = QLineEdit(self)
        self.name_input.move(200, 10)

    def hello(self):
        name = self.name_input.text()  # Получим текст из поля ввода
        self.label.setText(f"Привет, {name}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())