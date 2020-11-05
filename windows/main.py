from PyQt5 import QtWidgets, QtGui
from views.main_ui import Ui_MainWindow
import sys
import os
import json
from utils.helpers import validateJSON
import threading
from diglogs.about import AboutDialog


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, next, pchome):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('pchome小幫手-資料輸入')
        self.setWindowIcon(QtGui.QIcon('comics-ironman-hand_97416.ico'))

        # Bind event
        self.ui.submit_btn.clicked.connect(self.submit_btn_handler)
        self.ui.close_btn.clicked.connect(self.close_btn_handler)
        self.ui.clear_record.triggered.connect(self.clear_record_handler)
        self.ui.about.triggered.connect(self.about_show)

        # Diglogs
        self.aboutDialog = AboutDialog()

        # Next page
        self.next = next
        # StatusBar        
        self.pchome = pchome

        self.setup_data()

        # self.statusBar().showMessage('TEST Again!!!')
    def setup_data(self):
        if os.path.exists('record.json'):
            f = open('record.json')
            json_data = f.read()
            isValid = validateJSON(json_data)
            if isValid:
                form_data = json.loads(json_data)
                self.ui.email.setText(form_data['email'])
                self.ui.password.setText(form_data['password'])
                self.ui.target_url.setText(form_data['target_url'])
                self.ui.browser_qty.setValue(form_data['browser_qty'])
                self.ui.record.setChecked(form_data['record'])

    def about_show(self):
        self.aboutDialog.show()

    def close_btn_handler(self):
        import sys
        sys.exit(0)

    def submit_btn_handler(self):
        form_data = {
            'email': self.ui.email.text(),
            'password': self.ui.password.text(),
            'target_url': self.ui.target_url.text(),
            'browser_qty': self.ui.browser_qty.value(),
            'record': self.ui.record.isChecked()
        }
        if self.ui.record.isChecked():
            json_form_data = json.dumps(form_data)
            with open('record.json', 'w') as f:
                f.write(json_form_data)
        
        t = threading.Thread(name='auto start', target=self.pchome.run, args=[form_data])
        t.setDaemon(True)
        t.start()

        self.close()
        self.next()

    def clear_record_handler(self):
        if os.path.exists('record.json'):
            os.remove("record.json")
            self.clear_form()

    def clear_form(self):
        self.ui.email.clear()
        self.ui.password.clear()
        self.ui.target_url.clear()
        self.ui.browser_qty.setValue(1)
        self.ui.record.setChecked(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())