import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PIL import Image


SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')

        img = Image.open('orig.jpg')
        img.save('orig1.jpg')

        self.pixmap = QPixmap('orig.jpg')
        self.image = QLabel(self)
        self.image.move(140, 20)
        self.image.resize(200, 200)
        self.image.setPixmap(self.pixmap)

        self.r = QPushButton(self, )
        self.r.resize(100, 20)
        self.r.move(10, 30)
        self.r.setText('R')
        self.r.clicked.connect(self.rgb)

        self.g = QPushButton(self)
        self.g.resize(100, 20)
        self.g.move(10, 80)
        self.g.setText('G')
        self.g.clicked.connect(self.rgb)


        self.b = QPushButton(self)
        self.b.resize(100, 20)
        self.b.move(10, 130)
        self.b.setText('B')
        self.b.clicked.connect(self.rgb)

        self.a = QPushButton(self)
        self.a.resize(100, 20)
        self.a.move(10, 180)
        self.a.setText('ALL')
        self.a.clicked.connect(self.rgb)

        self.rot1 = QPushButton(self)
        self.rot1.resize(180, 20)
        self.rot1.move(0, 300)
        self.rot1.setText('Против часовой стрелки')
        self.rot1.clicked.connect(self.rotation)

        self.rot2 = QPushButton(self)
        self.rot2.resize(180, 20)
        self.rot2.move(220, 300)
        self.rot2.setText('По часовой стрелке')
        self.rot2.clicked.connect(self.rotation)

    def rgb(self):
        img = Image.open('orig.jpg')
        data = img.getdata()

        r = [(d[0], 0, 0) for d in data]
        g = [(0, d[1], 0) for d in data]
        b = [(0, 0, d[2]) for d in data]
        if self.sender().text() == 'R':
            img.putdata(r)
        elif self.sender().text() == 'G':
            img.putdata(g)
        elif self.sender().text() == 'B':
            img.putdata(b)
        else:
            img = Image.open('orig.jpg')
        img.save('orig1.jpg')
        self.image.setPixmap(QPixmap('orig1.jpg'))

    def rotation(self):
        img = Image.open('orig1.jpg')
        if self.sender().text() == 'Против часовой стрелки':
            img = img.rotate(90)
        else:
            img = img.rotate(-90)
        img.save('orig1.jpg')
        self.image.setPixmap(QPixmap('orig1.jpg'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())