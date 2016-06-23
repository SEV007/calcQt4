#Window Code
from __future__ import division #default float division
from PyQt4.QtCore import *
from PyQt4.QtGui import * #Widgets import

import sys

__author__ = "deus aka sev"
__license__ = "GPL"
__version__ = "1.0.1"

class Window(QWidget):

	def __init__(self):
		super(Window, self).__init__()

		#Change Window Title
		self.setWindowTitle("Tutorial PyQt")

		#Resize Window
		self.resize(400, 240  )

		#Move window
		self.move(200, 100)

		#Change Icon
		#self.setWindowIcon(QIcon("any.svg"))

		self.display = QLineEdit()

		btn1 = QPushButton("1", self)
		btn2 = QPushButton("2", self)
		btn3 = QPushButton("3", self)
		btn4 = QPushButton("4", self)
		btn5 = QPushButton("5", self)
		btn6 = QPushButton("6", self)
		btn7 = QPushButton("7", self)
		btn8 = QPushButton("8", self)
		btn9 = QPushButton("9", self)
		btn0 = QPushButton("0", self)

		btnDiv = QPushButton("/", self)
		btnMult = QPushButton("*", self)
		btnRest = QPushButton("-", self)
		btnSum = QPushButton("+", self)

		btnFp = QPushButton(",", self)
		btnDel = QPushButton("C", self)
		btnEq = QPushButton("=", self)


		#dlayout = QVBoxLayout(self) //double layout nesting solution
		grid = QGridLayout(self)
		
		grid.addWidget(btn1, 1, 0)
		grid.addWidget(btn2, 1, 1)
		grid.addWidget(btn3, 1, 2)
		grid.addWidget(btn4, 2, 0)
		grid.addWidget(btn5, 2, 1)
		grid.addWidget(btn6, 2, 2)
		grid.addWidget(btn7, 3, 0)
		grid.addWidget(btn8, 3, 1)
		grid.addWidget(btn9, 3, 2)
		grid.addWidget(btn0, 4, 1)
		
		grid.addWidget(btnDiv, 1, 3)
		grid.addWidget(btnMult, 2, 3)
		grid.addWidget(btnRest, 3, 3)
		grid.addWidget(btnSum, 4, 3)

		grid.addWidget(btnFp, 4, 2)
		grid.addWidget(btnDel, 4, 0)
		grid.addWidget(btnEq, 5, 0, 4, 4)

		#dlayout.addWidget(display)	//double layout nesting solution
		#dlayout.addLayout(grid)	//double layout nesting solution
		grid.addWidget(self.display, 0, 0, 1, 4)


		btn1.clicked.connect(self.btn1)
		btn2.clicked.connect(self.btn2)
		btn3.clicked.connect(self.btn3)
		btn4.clicked.connect(self.btn4)
		btn5.clicked.connect(self.btn5)
		btn6.clicked.connect(self.btn6)
		btn7.clicked.connect(self.btn7)
		btn8.clicked.connect(self.btn8)
		btn9.clicked.connect(self.btn9)
		btn0.clicked.connect(self.btn0)
		btnDiv.clicked.connect(self.btnDiv)
		btnMult.clicked.connect(self.btnMult)
		btnRest.clicked.connect(self.btnRest)
		btnSum.clicked.connect(self.btnSum)
		btnFp.clicked.connect(self.btnFp)
		btnDel.clicked.connect(self.btnDel)
		btnEq.clicked.connect(self.btnEq)

	def btn1(self):
		aux = self.display.text()
		self.display.setText(aux + "1")

	def btn2(self):
		aux = self.display.text()
		self.display.setText(aux + "2")

	def btn3(self):
		aux = self.display.text()
		self.display.setText(aux + "3")

	def btn4(self):
		aux = self.display.text()
		self.display.setText(aux + "4")

	def btn5(self):
		aux = self.display.text()
		self.display.setText(aux + "5")

	def btn6(self):
		aux = self.display.text()
		self.display.setText(aux + "6")

	def btn7(self):
		aux = self.display.text()
		self.display.setText(aux + "7")

	def btn8(self):
		aux = self.display.text()
		self.display.setText(aux + "8")

	def btn9(self):
		aux = self.display.text()
		self.display.setText(aux + "9")

	def btn0(self):
		aux = self.display.text()
		self.display.setText(aux + "0")

	def btnDiv(self):
		aux = self.display.text()
		self.display.setText(aux + "/")

	def btnMult(self):
		aux = self.display.text()
		self.display.setText(aux + "*")

	def btnRest(self):
		aux = self.display.text()
		self.display.setText(aux + "-")

	def btnSum(self):
		aux = self.display.text()
		self.display.setText(aux + "+")

	def btnFp(self):
		aux = self.display.text()
		self.display.setText(aux + ".")

	def btnDel(self):
		aux = ""
		self.display.setText("")

	def btnEq(self):
		aux = eval(str(self.display.text()))
		self.display.setText(str(aux))

	aux = ""

app = QApplication(sys.argv)

window = Window()
window.show()

#Mainloop keepalive app
sys.exit(app.exec_())
