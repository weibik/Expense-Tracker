# Jakub Szkola
#    2022
# Expense tracker

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

class MyWindow(QMainWindow):
    total = 0
    categories = ["parties", "car", "dates", "food", "books", "clothes", "other"]

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(960, 540, 600, 400)
        self.setWindowTitle("Expense Tracker")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.initUI()

    def error(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("ERROR!")
        self.msg.setInformativeText('PUT A NUMBER')
        self.msg.setWindowTitle("Error")
        self.msg.exec_()

    def clickAddExpenseButton(self):
        if self.expenseInput.text().isnumeric():
            self.total  += int(self.expenseInput.text())
        else:
            self.error()
        self.label.setText("Total spendings: " + str(self.total))
        self.expenseInput.clear()
        self.update()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Total spendings: " + str(self.total))
        self.label.move(250, 0)

        self.addExpenseButton = QtWidgets.QPushButton(self)
        self.addExpenseButton.setText("Add expense")
        self.addExpenseButton.move(250, 350)
        self.addExpenseButton.clicked.connect(self.clickAddExpenseButton)

        self.expenseInput = QtWidgets.QLineEdit(self)
        self.expenseInput.move (250, 300)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
