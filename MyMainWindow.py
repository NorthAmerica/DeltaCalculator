from Test import Ui_MainWindow
from PyQt5 import QtCore

class MyMainWindow(Ui_MainWindow):
	def setupUi(self, MainWindow):
		Ui_MainWindow.setupUi(self,MainWindow)
		_translate = QtCore.QCoreApplication.translate
		self.pushButton.clicked.connect(lambda: MainWindow.slotDock(self))


	def __init__(self):
		pass