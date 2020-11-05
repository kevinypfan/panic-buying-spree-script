from PyQt5 import QtCore, QtGui, QtWidgets
import views.main_ui
import views.shutdown_ui
import views.about_ui
import views.activate_ui
import json
import os
from helpers import validateJSON
from pchome_cookie import PchomePanic
import threading
from get_serial_number import getMachine_addr
from windows.utils import critical
import requests


class Application():
    def __init__(self):
        
        self.serial_code = getMachine_addr()

        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.main_ui = views.main_ui.Ui_MainWindow()
        self.main_ui.setupUi(self.MainWindow)
        self.ShotdownWindow = QtWidgets.QMainWindow()
        self.shutdown_ui = views.shutdown_ui.Ui_MainWindow()
        self.shutdown_ui.setupUi(self.ShotdownWindow)
        self.DialogAbout = QtWidgets.QDialog()
        self.about_ui = views.about_ui.Ui_Dialog()
        self.about_ui.setupUi(self.DialogAbout)
        self.ActivateWindow = QtWidgets.QMainWindow()
        self.activate_ui = views.activate_ui.Ui_MainWindow()
        self.activate_ui.setupUi(self.ActivateWindow)
        if self.is_activate():
            self.MainWindow.show()
        else:   
            self.activate_ui.serial_code.setText(getMachine_addr())
            self.ActivateWindow.show()
        self.clear_form()
        self.setup_app()
        self.bind_events()
        self.pchome = PchomePanic()
        sys.exit(self.app.exec_())

    def load_activate_code(self):
        if os.path.exists('activate_key'):
            f = open('activate_key')
            return f.read()
        return None

    def is_activate(self):
        activate_code = self.load_activate_code()
        if activate_code == None:
            return False
        else:
            response = requests.post('https://dev.kevins.fun/v1.0/activate/verify-code', json={'activate_code': activate_code, 'serial_code': getMachine_addr()})
            if response.json()['returnCode'] == '000000':
                return True
    
    def setup_app(self):
        if os.path.exists('record.json'):
            f = open('record.json')
            json_data = f.read()
            isValid = validateJSON(json_data)
            if isValid:
                form_data = json.loads(json_data)
                self.main_ui.email.setText(form_data['email'])
                self.main_ui.password.setText(form_data['password'])
                self.main_ui.target_url.setText(form_data['target_url'])
                self.main_ui.browser_qty.setValue(form_data['browser_qty'])
                self.main_ui.record.setChecked(form_data['record'])

    def about_show(self):
        self.serial_code = getMachine_addr()
        self.about_ui.serial_code.setText(self.serial_code)
        self.about_ui.activate_code.setText(self.load_activate_code())
        self.DialogAbout.show()

    def about_close(self):
        self.DialogAbout.close()

    def submit_btn_handler(self):
        form_data = {
            'email': self.main_ui.email.text(),
            'password': self.main_ui.password.text(),
            'target_url': self.main_ui.target_url.text(),
            'browser_qty': self.main_ui.browser_qty.value(),
            'record': self.main_ui.record.isChecked()
        }
        if self.main_ui.record.isChecked():
            json_form_data = json.dumps(form_data)
            with open('record.json', 'w') as f:
                f.write(json_form_data)
        self.MainWindow.close()
        self.ShotdownWindow.show()
        
        t = threading.Thread(name='auto start', target=self.pchome.run, args=[form_data])
        t.setDaemon(True)
        t.start()

        

    def close_btn_handler(self):
        self.pchome.stop()
        import sys
        sys.exit(0)
    
    def clear_record_handler(self):
        if os.path.exists('record.json'):
            os.remove("record.json")
            self.clear_form()

    def activate_submit_handler(self):
        response = requests.post('https://dev.kevins.fun/v1.0/activate/verify-code', json={'activate_code': self.activate_ui.activate_code.text(), 'serial_code': getMachine_addr()})
        if response.json()['returnCode'] == '000000':
            with open('activate_key', 'w') as f:
                f.write(self.activate_ui.activate_code.text())
            self.ActivateWindow.close()
            self.MainWindow.show()
        else:
            critical(content=f'{response.json()["returnMessage"]}({response.json()["returnCode"]})')

    def bind_events(self):
        self.main_ui.submit_btn.clicked.connect(self.submit_btn_handler)
        self.main_ui.close_btn.clicked.connect(self.close_btn_handler)
        self.main_ui.clear_record.triggered.connect(self.clear_record_handler)
        self.main_ui.about.triggered.connect(self.about_show)
        self.shutdown_ui.stop_app.clicked.connect(self.close_btn_handler)
        self.activate_ui.submit_btn.clicked.connect(self.activate_submit_handler)
        self.about_ui.ok_btn.clicked.connect(self.about_close)


    def clear_form(self):
        self.main_ui.email.clear()
        self.main_ui.password.clear()
        self.main_ui.target_url.clear()
        self.main_ui.browser_qty.setValue(1)
        self.main_ui.record.setChecked(False)
    

if __name__ == "__main__":
    qt_app = Application()
