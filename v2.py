from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from windows.activate import ActivateWindow
from windows.main import MainWindow
from windows.shutdown import ShutdownWindow
from tools.helpers import is_activate, load_activate_code, getMachine_addr
from pchome_cookie import PchomePanic
from momo_cookie import MomoPanic



app = QtWidgets.QApplication([])

pchome = PchomePanic()
momo = MomoPanic()

shutdownWindow = ShutdownWindow(pchome, momo)
mainWindow = MainWindow(shutdownWindow.show, pchome, momo)

if is_activate(load_activate_code(), getMachine_addr()):
    mainWindow.show()
    
else:   
    activateWindow = ActivateWindow(mainWindow.show)
    activateWindow.show()



sys.exit(app.exec_())