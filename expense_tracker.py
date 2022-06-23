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

suma = 0

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(960, 540, 600, 400)
win.setWindowTitle("Expense Tracker")
win.setWindowIcon(QtGui.QIcon("logo.png"))

label = QtWidgets.QLabel(win)
label.setText("Total spendings: " + str(suma))
label.move(250, 0)

addExpenseButton = QtWidgets.QPushButton(win)
addExpenseButton.setText("Add expense")
addExpenseButton.move(250, 350)

expenseInput = QtWidgets.QLineEdit(win)
expenseInput.setText("enter value")
expenseInput.setAlignment(QtCore.Qt.AlignCenter)
expenseInput.move (250, 300)

win.show()
sys.exit(app.exec_())

