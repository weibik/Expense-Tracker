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
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(960, 540, 600, 400)
        self.setWindowTitle("Expense Tracker")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Total spendings: " + str(suma))
        self.label.move(250, 0)

        self.addExpenseButton = QtWidgets.QPushButton(self)
        self.addExpenseButton.setText("Add expense")
        self.addExpenseButton.move(250, 350)

        self.expenseInput = QtWidgets.QLineEdit(self)
        self.expenseInput.setText("enter value")
        self.expenseInput.setAlignment(QtCore.Qt.AlignCenter)
        self.expenseInput.move (250, 300)

    def clickAddExpenseButton():
        print("clicked")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

suma = 0
categories = ["parties", "car", "dates", "food", "books", "clothes","other"]


window()
