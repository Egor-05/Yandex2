import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QPlainTextEdit, QPushButton


class Example(QWidget):

    lst = []

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(480, 370, 480, 370)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.te = QPlainTextEdit(self)
        self.te.move(200, 20)
        self.te.resize(250, 350)

        self.btn = QPushButton('Создать новый', self)
        self.btn.resize(160, 20)
        self.btn.move(20, 60)
        self.btn.clicked.connect(self.create_file)

        self.btn1 = QPushButton('Сохранить файл', self)
        self.btn1.resize(160, 20)
        self.btn1.move(20, 100)
        self.btn1.clicked.connect(self.end_work)

        self.btn2 = QPushButton('Открыть файл', self)
        self.btn2.resize(160, 20)
        self.btn2.move(20, 140)
        self.btn2.clicked.connect(self.open_file)

        self.le = QLineEdit(self)
        self.le.resize(160, 20)
        self.le.move(20, 20)

    def create_file(self):
        self.f = open(self.le.text(), 'w')

    def open_file(self):
        with open(self.le.text(), 'r') as f:
            text = f.read()
        self.te.appendPlainText(text)
        self.f = open(self.le.text(), 'w')


    def end_work(self):
        self.f.write(self.te.toPlainText())
        self.f.close()
        self.te.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())