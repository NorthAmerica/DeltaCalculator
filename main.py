import sys
import Test
import MyMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from time import time
from MonteCarlo import *

def newFunction(self):
    begin = time()
    try:
        mc99 = MonteCarlo(99.99)
        mc100 = MonteCarlo(100)
        mc101 = MonteCarlo(100.01)
        gaussNumList =  mc99.gaussNum();
        result1 = mc99.calculate(gaussNumList)
        result2 = mc100.calculate(gaussNumList)
        result3 = mc101.calculate(gaussNumList)
    except NameError as ex:
        print(ex)
    k1 = (result3 - result2)/0.01
    k2 = (result2 - result1)/0.01
    kl=[k1,k2]
    final = sum(kl)/len(kl)
    total_time = time() - begin
    _translate = QtCore.QCoreApplication.translate
    self.label_2.setText(_translate("MainWindow", str(result1)))
    self.label_4.setText(_translate("MainWindow", str(result2)))
    self.label_6.setText(_translate("MainWindow", str(result3)))
    self.label_8.setText(_translate("MainWindow", str(final)))
    self.label_10.setText(_translate("MainWindow", str(total_time)))
    return "This is a newFunction"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.slotDock = newFunction
    ui = MyMainWindow.MyMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
