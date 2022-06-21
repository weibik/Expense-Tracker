# Jakub Szkola
#    2022
# Expense tracker

# Libraries used: 
# - pandas
# - matplotlib

import imp
from pandas import *
import matplotlib as mpb
from tkinter import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(960, 540, 600, 400)
    win.setWindowTitle("expense tracker")

    label = QtWidgets.QLabel(win)
    label.setText("Total spendings:")
    label.move(100, 100)

    win.show()
    sys.exit(app.exec_())

window()