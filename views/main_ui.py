# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 337)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 761, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 20, 581, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pchome_email = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pchome_email.setText("")
        self.pchome_email.setObjectName("pchome_email")
        self.gridLayout.addWidget(self.pchome_email, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pchome_password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pchome_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pchome_password.setObjectName("pchome_password")
        self.gridLayout.addWidget(self.pchome_password, 1, 2, 1, 1)
        self.pchome_target_url = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pchome_target_url.setObjectName("pchome_target_url")
        self.gridLayout.addWidget(self.pchome_target_url, 2, 2, 1, 1)
        self.pchome_browser_qty = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.pchome_browser_qty.setObjectName("pchome_browser_qty")
        self.gridLayout.addWidget(self.pchome_browser_qty, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.excute_date = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.excute_date.setDateTime(QtCore.QDateTime(QtCore.QDate(1997, 1, 1), QtCore.QTime(14, 0, 0)))
        self.excute_date.setDate(QtCore.QDate(1997, 1, 1))
        self.excute_date.setObjectName("excute_date")
        self.gridLayout.addWidget(self.excute_date, 4, 2, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 200, 160, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pchome_record = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.pchome_record.setObjectName("pchome_record")
        self.horizontalLayout_2.addWidget(self.pchome_record)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(420, 220, 241, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pchome_submit_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pchome_submit_btn.setObjectName("pchome_submit_btn")
        self.horizontalLayout.addWidget(self.pchome_submit_btn)
        self.pchome_close_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pchome_close_btn.setEnabled(True)
        self.pchome_close_btn.setObjectName("pchome_close_btn")
        self.horizontalLayout.addWidget(self.pchome_close_btn)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(410, 220, 241, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.momo_submit_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.momo_submit_btn.setObjectName("momo_submit_btn")
        self.horizontalLayout_4.addWidget(self.momo_submit_btn)
        self.momo_close_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.momo_close_btn.setEnabled(True)
        self.momo_close_btn.setObjectName("momo_close_btn")
        self.horizontalLayout_4.addWidget(self.momo_close_btn)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 10, 581, 181))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.momo_browser_qty = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.momo_browser_qty.setObjectName("momo_browser_qty")
        self.gridLayout_4.addWidget(self.momo_browser_qty, 4, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 4, 0, 1, 1)
        self.momo_email = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.momo_email.setText("")
        self.momo_email.setObjectName("momo_email")
        self.gridLayout_4.addWidget(self.momo_email, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)
        self.momo_target_url = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.momo_target_url.setObjectName("momo_target_url")
        self.gridLayout_4.addWidget(self.momo_target_url, 2, 2, 1, 1)
        self.momo_password = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.momo_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.momo_password.setObjectName("momo_password")
        self.gridLayout_4.addWidget(self.momo_password, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.momo_target_id = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.momo_target_id.setObjectName("momo_target_id")
        self.gridLayout_4.addWidget(self.momo_target_id, 3, 2, 1, 1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(70, 200, 160, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.momo_record = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.momo_record.setObjectName("momo_record")
        self.horizontalLayout_5.addWidget(self.momo_record)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pchome_clear_record = QtWidgets.QAction(MainWindow)
        self.pchome_clear_record.setObjectName("pchome_clear_record")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.momo_clear_record = QtWidgets.QAction(MainWindow)
        self.momo_clear_record.setObjectName("momo_clear_record")
        self.menu.addAction(self.pchome_clear_record)
        self.menu.addAction(self.momo_clear_record)
        self.menu_2.addAction(self.about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "會員帳號："))
        self.label_4.setText(_translate("MainWindow", "瀏覽器數量："))
        self.label_3.setText(_translate("MainWindow", "目標網址："))
        self.label_2.setText(_translate("MainWindow", "會員密碼："))
        self.label_5.setText(_translate("MainWindow", "執行時間："))
        self.excute_date.setDisplayFormat(_translate("MainWindow", "yyyy/M/d HH:mm:ss"))
        self.pchome_record.setText(_translate("MainWindow", "記錄此次輸入內容"))
        self.pchome_submit_btn.setText(_translate("MainWindow", "開始執行"))
        self.pchome_close_btn.setText(_translate("MainWindow", "結束"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pchome"))
        self.momo_submit_btn.setText(_translate("MainWindow", "開始執行"))
        self.momo_close_btn.setText(_translate("MainWindow", "結束"))
        self.label_14.setText(_translate("MainWindow", "瀏覽器數量："))
        self.label_15.setText(_translate("MainWindow", "會員帳號："))
        self.label_16.setText(_translate("MainWindow", "會員密碼："))
        self.label_17.setText(_translate("MainWindow", "目標網址："))
        self.label_18.setText(_translate("MainWindow", "目標按鈕："))
        self.momo_record.setText(_translate("MainWindow", "記錄此次輸入內容"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Momo"))
        self.menu.setTitle(_translate("MainWindow", "設定"))
        self.menu_2.setTitle(_translate("MainWindow", "說明"))
        self.pchome_clear_record.setText(_translate("MainWindow", "清除 Pchome紀錄"))
        self.about.setText(_translate("MainWindow", "關於"))
        self.momo_clear_record.setText(_translate("MainWindow", "清除 Momo紀錄"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
