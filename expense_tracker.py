# Jakub Szkola
#    2022
# Expense tracker

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class MyWindow(QMainWindow):
    total = 0
    parties = car = dates = food = books = clothes = others = 0
    categ = ["Parties", "Car", "Dates", "Food", "Books", "Clothes", "Others"]

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(960, 540, 600, 400)
        self.setWindowTitle("Expense Tracker")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.initUI()

    def createChart(self):
        self.chartLayout = QtWidgets.QHBoxLayout()

        series = QPieSeries()
        series.append(self.categ[0], self.parties)
        series.append(self.categ[1], self.car)
        series.append(self.categ[2], self.dates)
        series.append(self.categ[3], self.food)
        series.append(self.categ[4], self.books)
        series.append(self.categ[5], self.clothes)
        series.append(self.categ[6], self.others)
        series.setLabelsVisible(True)

        series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
        i = 0
        for slice in series.slices():
            slice.setLabel(self.categ[i] + " - {:.2f}%".format(100 * slice.percentage()))
            i += 1

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Expenses in different categories")
        chart.legend().setVisible(True)

        chart.legend().markers(series)[0].setLabel("Parties")
        chart.legend().markers(series)[1].setLabel("Cars")
        chart.legend().markers(series)[2].setLabel("Dates")
        chart.legend().markers(series)[3].setLabel("Food")
        chart.legend().markers(series)[4].setLabel("Books")
        chart.legend().markers(series)[5].setLabel("Clothes")
        chart.legend().markers(series)[6].setLabel("Others")

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        backButton = QtWidgets.QPushButton(self)
        backButton.setText("Back")
        backButton.clicked.connect(self.initUI)

        self.chartLayout.addWidget(chartview)
        self.setLayout(self.chartLayout)
        #self.setCentralWidget(chartview)


    def errorWithInput(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("WRONG FORMAT!")
        self.msg.setInformativeText('PUT A NUMBER!')
        self.msg.setWindowTitle("Error")
        self.msg.exec_()

    def clickAddExpenseButton(self):
        if self.expenseInput.text().isnumeric():
            value = int(self.expenseInput.text())
            self.total  += value

            choice = str(self.boxWithcategories.currentText())
            match choice:
                case 'Parties':
                    self.parties += value
                case 'Car':
                    self.car += value
                case 'Dates':
                    self.dates += value
                case 'Food':
                    self.food += value
                case 'Books':
                    self.books += value
                case 'Clothes':
                    self.clothes += value
                case 'Others':
                    self.others += value
        else:
            self.errorWithInput()
        self.label.setText("Total spendings: " + str(self.total))
        #self.t.setText("Parties: " + str(self.parties))
        self.expenseInput.clear()
        self.update()

    def clickClearButton(self):
        self.total = 0
        self.label.setText("Total spendings: " + str(self.total))

    def initUI(self):
        self.mainLayout = QtWidgets.QHBoxLayout()
        
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

        self.graphButton = QtWidgets.QPushButton(self)
        self.graphButton.setText("Show graph")
        self.graphButton.setGeometry(475, 350, 100, 36)
        self.graphButton.clicked.connect(self.createChart)

        self.expenseInput = QtWidgets.QLineEdit(self)
        self.expenseInput.move (250, 300)

        self.boxWithcategories = QtWidgets.QComboBox(self)
        self.boxWithcategories.setGeometry(350, 351, 80, 34)
        categories = self.categ
        

        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.addExpenseButton)
        self.mainLayout.addWidget(self.clearButton)
        self.mainLayout.addWidget(self.graphButton)
        self.mainLayout.addWidget(self.expenseInput)
        self.mainLayout.addWidget(self.boxWithcategories)

        self.setLayout(self.mainLayout)
        

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
