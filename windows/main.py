from PyQt5 import QtWidgets, QtGui
from views.main_ui import Ui_MainWindow
import sys
import os
import json
from tools.helpers import validateJSON
import threading
from diglogs.about import AboutDialog


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
            'record': self.ui.pchome_record.isChecked()
        }
        if self.ui.pchome_record.isChecked():
            json_form_data = json.dumps(form_data)
            with open('pchome_record.json', 'w') as f:
                f.write(json_form_data)
        
        t = threading.Thread(name='auto start', target=self.pchome.run, args=[form_data])
        t.setDaemon(True)
        t.start()

        self.close()
        self.next()


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