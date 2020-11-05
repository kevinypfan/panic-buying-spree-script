from PyQt5 import QtWidgets, QtGui
from views.activate_ui import Ui_MainWindow
import sys
import requests
from windows.utils import critical
from utils.helpers import getMachine_addr
from windows.main import MainWindow


class ActivateWindow(QtWidgets.QMainWindow):
    def __init__(self, next):
        super(ActivateWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('pchome小幫手-啟動序號輸入')
        self.setWindowIcon(QtGui.QIcon('comics-ironman-hand_97416.ico'))

        # Bind event
        self.ui.submit_btn.clicked.connect(self.activate_submit_handler)
        self.ui.copy_btn.clicked.connect(self.copyText)

        # Next window
        self.next = next

        self.setup_data()
        # StatusBar
        # self.statusBar().showMessage('TEST Again!!!')
    def setup_data(self):
        self.ui.serial_code.setText(getMachine_addr())

    def copyText(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.ui.serial_code.text())

    def activate_submit_handler(self):
        response = requests.post('https://dev.kevins.fun/v1.0/activate/verify-code', json={'activate_code': self.ui.activate_code.text(), 'serial_code': getMachine_addr()})
        if response.json()['returnCode'] == '000000':
            with open('activate_key', 'w') as f:
                f.write(self.ui.activate_code.text())
            self.close()
            self.next()
        else:
            critical(content=f'{response.json()["returnMessage"]}({response.json()["returnCode"]})')
