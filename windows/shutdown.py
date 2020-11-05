from PyQt5 import QtWidgets, QtGui
from views.shutdown_ui import Ui_MainWindow
import sys


class ShutdownWindow(QtWidgets.QMainWindow):
    def __init__(self, pchome):
        super(ShutdownWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('pchome小幫手-結束按鈕')
        self.setWindowIcon(QtGui.QIcon('comics-ironman-hand_97416.ico'))

        # Bind event
        self.ui.stop_app.clicked.connect(self.close_btn_handler)
        # StatusBar
        # self.statusBar().showMessage('TEST Again!!!')
        self.pchome = pchome

    def close_btn_handler(self):
        self.pchome.stop()
        import sys
        sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ShutdownWindow()
    window.show()
    sys.exit(app.exec_())