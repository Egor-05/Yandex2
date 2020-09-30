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
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 80)
        self.btn.clicked.connect(self.count)

        self.label = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label.setText("Первое число(целое):")
        self.label.move(20, 25)

        self.name_input = QLineEdit(self)
        self.name_input.move(20, 40)

        self.label2 = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label2.setText("Второе число(целое):")
        self.label2.move(20, 105)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(20, 120)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(275, 25)
        self.LCD_count.display(0)

        self.LCD_count1 = QLCDNumber(self)
        self.LCD_count1.move(275, 65)
        self.LCD_count1.display(0)

        self.LCD_count2 = QLCDNumber(self)
        self.LCD_count2.move(275, 105)
        self.LCD_count2.display(0)

        self.LCD_count3 = QLCDNumber(self)
        self.LCD_count3.move(275, 145)
        self.LCD_count3.display(0)



    def count(self):
        a = int(self.name_input.text())
        b = int(self.name_input2.text())
        self.LCD_count.display(a + b)
        self.LCD_count1.display(a - b)
        self.LCD_count2.display(a * b)
        if b != 0:
            self.LCD_count3.display(a / b)
        else:
            self.LCD_count3.display('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())