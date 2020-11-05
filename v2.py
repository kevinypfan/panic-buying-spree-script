from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from windows.activate import ActivateWindow
from windows.main import MainWindow
from windows.shutdown import ShutdownWindow
from utils.helpers import is_activate, load_activate_code, getMachine_addr
from pchome_cookie import PchomePanic



app = QtWidgets.QApplication([])

pchome = PchomePanic()

shutdownWindow = ShutdownWindow(pchome)
mainWindow = MainWindow(shutdownWindow.show, pchome)

if is_activate(load_activate_code(), getMachine_addr()):
    mainWindow.show()
    
else:   
    activateWindow = ActivateWindow(mainWindow.show)
    activateWindow.show()



sys.exit(app.exec_())