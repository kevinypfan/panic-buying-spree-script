from PyQt5 import QtWidgets, QtGui, QtCore
from views.main_ui import Ui_MainWindow
import sys
import os
import json
from tools.helpers import validateJSON
import threading
from diglogs.about import AboutDialog
import time


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, next, pchome, momo):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('pchome小幫手-資料輸入')
        self.setWindowIcon(QtGui.QIcon('comics-ironman-hand_97416.ico'))

        # Bind event
        self.ui.pchome_submit_btn.clicked.connect(self.pchome_submit_btn_handler)
        self.ui.momo_submit_btn.clicked.connect(self.momo_submit_btn_handler)
        self.ui.pchome_close_btn.clicked.connect(self.close_btn_handler)
        self.ui.momo_close_btn.clicked.connect(self.close_btn_handler)
        self.ui.pchome_clear_record.triggered.connect(self.clear_record_handler('pchome'))
        self.ui.momo_clear_record.triggered.connect(self.clear_record_handler('momo'))
        self.ui.about.triggered.connect(self.about_show)

        # Diglogs
        self.aboutDialog = AboutDialog()

        # Next page
        self.next = next
        # StatusBar        
        self.pchome = pchome
        self.momo = momo

        self.setup_pchome_data()
        self.setup_momo_data()

        # self.statusBar().showMessage('TEST Again!!!')

    def setup_momo_data(self):
        if os.path.exists('momo_record.json'):
            f = open('momo_record.json')
            json_data = f.read()
            isValid = validateJSON(json_data)
            if isValid:
                form_data = json.loads(json_data)
                self.ui.momo_email.setText(form_data['email'])
                self.ui.momo_password.setText(form_data['password'])
                self.ui.momo_target_url.setText(form_data['target_url'])
                self.ui.momo_target_id.setText(form_data['target_id'])
                self.ui.momo_browser_qty.setValue(form_data['browser_qty'])
                self.ui.momo_record.setChecked(form_data['record'])

    def setup_pchome_data(self):
        currentTime = QtCore.QDateTime.currentDateTime()
        if os.path.exists('pchome_record.json'):
            f = open('pchome_record.json')
            json_data = f.read()
            isValid = validateJSON(json_data)
            if isValid:
                form_data = json.loads(json_data)
                self.ui.pchome_email.setText(form_data['email'])
                self.ui.pchome_password.setText(form_data['password'])
                self.ui.pchome_target_url.setText(form_data['target_url'])
                self.ui.pchome_browser_qty.setValue(form_data['browser_qty'])
                self.ui.pchome_record.setChecked(form_data['record'])
                self.ui.excute_date.setDateTime(currentTime)


    def about_show(self):
        self.aboutDialog.show()

    def close_btn_handler(self):
        import sys
        sys.exit(0)

    def pchome_submit_btn_handler(self):
        

        form_data = {
            'email': self.ui.pchome_email.text(),
            'password': self.ui.pchome_password.text(),
            'target_url': self.ui.pchome_target_url.text(),
            'browser_qty': self.ui.pchome_browser_qty.value(),
            'record': self.ui.pchome_record.isChecked(),
        }
        if self.ui.pchome_record.isChecked():
            json_form_data = json.dumps(form_data)
            with open('pchome_record.json', 'w') as f:
                f.write(json_form_data)

        form_data['excute_date'] = self.ui.excute_date.dateTime()
        self.pchome.load_credentials(form_data)
        self.run_thread('first_login', self.pchome.first_login)
        self.close()
        self.next()
        currentTime = QtCore.QDateTime.currentDateTime()
        while currentTime < form_data['excute_date']:
            print(f"{currentTime} vs {form_data['excute_date']}")
            time.sleep(0.6)
            currentTime = QtCore.QDateTime.currentDateTime()

        self.run_thread('thread_run', self.pchome.thread_run)
        
        # self.run_chrome(form_data)
    

    def run_thread(self, thread_name, excute_func, *args):
        t = threading.Thread(name=thread_name, target=excute_func, args=args)
        t.setDaemon(True)
        t.start()



    def momo_submit_btn_handler(self):
        form_data = {
            'email': self.ui.momo_email.text(),
            'password': self.ui.momo_password.text(),
            'target_url': self.ui.momo_target_url.text(),
            'target_id': self.ui.momo_target_id.text(),
            'browser_qty': self.ui.momo_browser_qty.value(),
            'record': self.ui.momo_record.isChecked()
        }
        if self.ui.momo_record.isChecked():
            json_form_data = json.dumps(form_data)
            with open('momo_record.json', 'w') as f:
                f.write(json_form_data)
        
        t = threading.Thread(name='auto start', target=self.momo.run, args=[form_data])
        t.setDaemon(True)
        t.start()

        self.close()
        self.next()

    def clear_record_handler(self, tab):
        def func():
            if os.path.exists(f'{tab}_record.json'):
                os.remove(f'{tab}_record.json')
                self.clear_form(tab)
        return func

    def clear_form(self, tab):
        if tab == 'momo':
            self.ui.momo_email.clear()
            self.ui.momo_password.clear()
            self.ui.momo_target_url.clear()
            self.ui.momo_target_id.clear()
            self.ui.momo_browser_qty.setValue(1)
            self.ui.momo_record.setChecked(False)
        if tab == 'pchome':
            self.ui.pchome_email.clear()
            self.ui.pchome_password.clear()
            self.ui.pchome_target_url.clear()
            self.ui.pchome_browser_qty.setValue(1)
            self.ui.pchome_record.setChecked(False)

# if __name__ == '__main__':
#     app = QtWidgets.QApplication([])
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())