from PyQt5 import QtWidgets, QtGui
from views.about_ui import Ui_Dialog
import sys
from utils.helpers import getMachine_addr, load_activate_code


class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('pchome小幫手-啟動序號輸入')
        self.setWindowIcon(QtGui.QIcon('comics-ironman-hand_97416.ico'))

        # Bind event
        self.ui.ok_btn.clicked.connect(self.close)
        # StatusBar
        # self.statusBar().showMessage('TEST Again!!!')
        self.setup_data()

    def setup_data(self):
        self.serial_code = getMachine_addr()
        self.ui.serial_code.setText(self.serial_code)
        self.ui.activate_code.setText(load_activate_code())
