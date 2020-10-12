import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(410, 310, 410, 310)
        self.setWindowTitle('QSlider')

        sld = QSlider(self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 30, 30, 200)
        sld.move(20, 20)
        sld.setValue(50)
        sld.valueChanged[int].connect(self.changeValue)

        self.image = QLabel(self)
        self.image.resize(300, 300)
        self.image.move(70, 0)
        self.pixmap = QPixmap('image1.png')
        self.image.setPixmap(self.pixmap)

        self.drawSmile()

    def drawSmile(self):
        width = 300
        height = 300
        im = Image.new('RGBA', (width, height), '#FFFFFF')
        draw = ImageDraw.Draw(im)
        draw.ellipse(((0, 0), (300, 300)), outline='#FF0000')
        draw.ellipse(((50, 50), (125, 125)), outline="#FF0000")
        draw.ellipse(((175, 50), (250, 125)), outline="#FF0000")
        draw.arc(((50, 200), (280, 250)), 60, 190, fill='#FF0000')
        im.save('image1.png', 'PNG')
        self.pixmap = QPixmap('image1.png')
        self.image.setPixmap(self.pixmap)

    def changeValue(self, value):
        width = 300 * value / 50
        height = 300 * value / 50
        im = Image.open('image1.png')
        im.save('im.png', 'PNG')
        im = Image.open('im.png')
        im = im.resize((int(width), int(height)))
        im.save('im.png', 'PNG')
        self.pixmap = QPixmap('im.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())