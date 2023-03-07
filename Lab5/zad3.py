import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QGridLayout, QLineEdit, QApplication)
from matplotlib.pyplot import plot, show
from scipy import interpolate
from numpy import arange, exp


class Program(QWidget):
    def __init__(self):
        super().__init__()

        self.lbl1 = QLabel('Podaj: xp,xk,krok')
        self.lbl2 = QLabel('Uruchom')
        self.btn1 = QPushButton('Go')
        self.text1 = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.lbl1, 1, 0)
        grid.addWidget(self.text1, 1, 1)

        grid.addWidget(self.lbl2, 2, 0)
        grid.addWidget(self.btn1, 2, 1)

        self.setLayout(grid)

        self.btn1.clicked.connect(self.btn1Clicked)

        self.setGeometry(300, 300, 450, 150)
        self.setWindowTitle('Przykład: pole/przycisk')
        self.show()

    def btn1Clicked(self):
        sender = self.sender()
        txt1 = self.text1.text()
        txt1split = txt1.split(',')
        txt1final = 'xp=' + txt1split[0] + ' xk=' + txt1split[1] + ' krok=' + txt1split[2]
        self.text1.clear()
        self.text1.insert(txt1final)
        xp = float(txt1split[0])
        xk = float(txt1split[1])
        k = float(txt1split[2])
        self.interpolacja(xp, xk, k)
        print(float(txt1split[0]), float(txt1split[1]), float(txt1split[2]))
        print('Nacisnieto przycisk:', sender.text())
        print(txt1final)

    def interpolacja(self, xp, xk, k):
        print('xp, xk, k: ', xp, xk, k)
        x = arange(xp, xk, 1)
        print('x=', x)
        y = exp(-x / 3.0)
        f = interpolate.interp1d(x, y)
        xnew = arange(xp, x[-1], k)
        print('xnew= ', xnew)
        ynew = f(xnew)
        print('ynew= ', ynew)
        plot(x, y, 'o', xnew, ynew, '-')
        show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    sys.exit(app.exec_())
