from PyQt5 import QtCore, QtGui, QtWidgets
import main_ui
import shutdown_ui
import about_ui
import activate_ui
import json
import os
from helpers import validateJSON
from pchome_cookie import PchomePanic
import threading
from get_serial_number import getMachine_addr

ACTIVATE_CODE = "abc123"

class Application():
    def __init__(self):
        
        self.serial_code = None

        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.main_ui = main_ui.Ui_MainWindow()
        self.main_ui.setupUi(self.MainWindow)
        self.ShotdownWindow = QtWidgets.QMainWindow()
        self.shutdown_ui = shutdown_ui.Ui_MainWindow()
        self.shutdown_ui.setupUi(self.ShotdownWindow)
        self.DialogAbout = QtWidgets.QDialog()
        self.about_ui = about_ui.Ui_Dialog()
        self.about_ui.setupUi(self.DialogAbout)
        self.ActivateWindow = QtWidgets.QMainWindow()
        self.activate_ui = activate_ui.Ui_MainWindow()
        self.activate_ui.setupUi(self.ActivateWindow)
        self.ActivateWindow.show()
        self.clear_form()
        self.setup_app()
        self.bind_events()
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

    def about_show(self):
        self.serial_code = getMachine_addr()
        self.about_ui.serial_code.setText(self.serial_code)
        self.about_ui.activate_code.setText(ACTIVATE_CODE)
        self.DialogAbout.show()

    def about_close(self):
        self.DialogAbout.close()

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

    def activate_submit_handler(self):
        print('activate_submit_handler')
        if self.activate_ui.activate_code.text() == ACTIVATE_CODE:
            self.ActivateWindow.close()
            self.MainWindow.show()
        else:
            self.critical()

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
    
    def critical(self, title="錯誤", content="輸入之序號有誤！"):
        # reply = QMessageBox.critical(self,'错误','这是一个错误消息对话框', QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore , QMessageBox.Retry)
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setText(content)
        msgBox.addButton('確定', QtWidgets.QMessageBox.AcceptRole)
        # msgBox.setDefaultButton(QMessageBox.Retry)
        # msgBox.setDetailedText('这是详细的信息：学点编程吧，我爱你！')
        reply = msgBox.exec() 
        print(reply)
        # if reply == QMessageBox.Retry:
        #     self.la.setText('你选择了Retry！') 
        # elif reply == QMessageBox.Abort:
        #     self.la.setText('你选择了Abort！')
        # else:
        #     self.la.setText('你选择了Ignore！')

if __name__ == "__main__":
    qt_app = Application()
