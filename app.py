from PyQt5 import QtCore, QtGui, QtWidgets
import main_ui
import shutdown_ui
import json
import os
from helpers import validateJSON
from pchome_cookie import PchomePanic
import threading

class Application():
    def __init__(self):
        
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.main_ui = main_ui.Ui_MainWindow()
        self.main_ui.setupUi(self.MainWindow)
        self.ShotdownWindow = QtWidgets.QMainWindow()
        self.shutdown_ui = shutdown_ui.Ui_MainWindow()
        self.shutdown_ui.setupUi(self.ShotdownWindow)
        self.clear_form()
        self.setup_app()
        self.bind_events()
        self.MainWindow.show()
        self.pchome = PchomePanic()
        sys.exit(self.app.exec_())

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


    def submit_btn_handler(self):
        print('submit')
        form_data = {
            'email': self.main_ui.email.text(),
            'password': self.main_ui.password.text(),
            'target_url': self.main_ui.target_url.text(),
            'browser_qty': self.main_ui.browser_qty.value(),
            'record': self.main_ui.record.isChecked()
        }
        print(form_data)
        json_form_data = json.dumps(form_data)
        with open('record.json', 'w') as f:
            f.write(json_form_data)
        self.MainWindow.close()
        self.ShotdownWindow.show()
        
        t = threading.Thread(name='auto start', target=self.pchome.run, args=[form_data])
        t.setDaemon(True)
        t.start()

        

    def close_btn_handler(self):
        print('close')
        self.pchome.stop()
        import sys
        sys.exit(0)
    
    def clear_record_handler(self):
        os.remove("record.json")
        self.clear_form()

    def bind_events(self):
        self.main_ui.submit_btn.clicked.connect(self.submit_btn_handler)
        self.main_ui.close_btn.clicked.connect(self.close_btn_handler)
        self.main_ui.clear_record.triggered.connect(self.clear_record_handler)
        self.shutdown_ui.stop_app.clicked.connect(self.close_btn_handler)


    def clear_form(self):
        self.main_ui.email.clear()
        self.main_ui.password.clear()
        self.main_ui.target_url.clear()
        self.main_ui.browser_qty.setValue(1)
        self.main_ui.record.setChecked(False)

if __name__ == "__main__":
    qt_app = Application()