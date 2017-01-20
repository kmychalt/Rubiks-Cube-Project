import sys
import cube
from enum import Enum
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import SIGNAL
 
qtCreatorFile = "rubiks_main.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) 
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.tableWidget.item(1,0).setBackground(QtGui.QColor(125,125,125))
        #self.connect(self.randomButton, SIGNAL("clicked()"), self.randomButtonClicked)
        self.connect(self.tableWidget.item(1,0), SIGNAL("clicked()"), self.tableItemClicked)
        
    def tableItemClicked(self):
        Color = Enum('Color', 'red blue white yellow green orange')
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())