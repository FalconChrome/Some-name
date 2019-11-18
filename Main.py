import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, Qt
from PyQt5.QtWidgets import QApplication, QWidget

SCREEN_SIZE = [400, 400]


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui',self)
        self.initUi()

    def initUi(self):
        self.setGeometry(400, 200, *SCREEN_SIZE)

        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(randint(50, SCREEN_SIZE[0]),
                      randint(50, SCREEN_SIZE[1]), *(randint(1, 100),) * 2)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())