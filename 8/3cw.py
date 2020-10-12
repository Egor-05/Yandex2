import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setGeometry(410, 310, 410, 310)
        self.setWindowTitle('QSlider')

        im = Image.open("image.png")
        im.save('image1.png', 'PNG')

        sld = QSlider(self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 30, 30, 200)
        sld.move(20, 20)
        sld.valueChanged[int].connect(self.changeValue)

        self.image = QLabel(self)
        self.image.resize(300, 300)
        self.image.move(70, 0)
        self.pixmap = QPixmap('image1.png')
        self.image.setPixmap(self.pixmap)

    def changeValue(self, value):
        im = Image.open("image1.png")
        pixels = im.load()
        x, y = im.size
        alpha = im.split()[-1]
        print(alpha)
        im.save('image1.png', 'PNG')
        self.pixmap = QPixmap('image1.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())