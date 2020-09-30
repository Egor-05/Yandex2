import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(375, 70, 375, 70)
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 20)
        self.btn.clicked.connect(self.count)

        self.label = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label.setText("Выражение:")
        self.label.move(40, 5)

        self.name_input = QLineEdit(self)
        self.name_input.move(40, 20)

        self.label2 = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label2.setText("Решение:")
        self.label2.move(232, 5)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(232, 20)

    def count(self):
        self.name_input2.setText(str(int(eval(self.name_input.text().replace(' ', '')))))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())