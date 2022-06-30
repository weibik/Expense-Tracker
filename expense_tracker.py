# Jakub Szkola
#    2022
# Expense tracker

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

class MyWindow(QMainWindow):
    total = 0

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(960, 540, 600, 400)
        self.setWindowTitle("Expense Tracker")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.initUI()

    def error(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("WRONG FORMAT!")
        self.msg.setInformativeText('PUT A NUMBER!')
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

    def clickClearButton(self):
        self.total = 0
        self.label.setText("Total spendings: " + str(self.total))

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Total spendings: " + str(self.total))
        self.label.move(250, 0)

        self.addExpenseButton = QtWidgets.QPushButton(self)
        self.addExpenseButton.setText("Add expense")
        self.addExpenseButton.setGeometry(250, 350, 100, 36)
        self.addExpenseButton.clicked.connect(self.clickAddExpenseButton)

        self.clearButton = QtWidgets.QPushButton(self)
        self.clearButton.setText("Clear")
        self.clearButton.setGeometry(25, 350, 100, 36)
        self.clearButton.clicked.connect(self.clickClearButton)

        self.expenseInput = QtWidgets.QLineEdit(self)
        self.expenseInput.move (250, 300)

        self.boxWithcategories = QtWidgets.QComboBox(self)
        self.boxWithcategories.setGeometry(350, 351, 80, 34)
        categories = ["Parties", "Car", "Dates", "Food", "Books", "Clothes", "Other"]
        
        
        ### Here are the things to set center alignment within comboBox
        self.boxWithcategories.setEditable(True)
        self.boxWithcategories.addItems(categories)
        line_edit = self.boxWithcategories.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
