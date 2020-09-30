import sys

from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup, QVBoxLayout, QLCDNumber, QListWidget
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = 0

    def initUI(self):
        self.setGeometry(375, 100, 375, 100)
        self.setWindowTitle('Фокус со словами')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())