from PyQt5 import QtWidgets

def critical(title="錯誤", content="輸入之序號有誤！"):
    # reply = QMessageBox.critical(self,'错误','这是一个错误消息对话框', QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore , QMessageBox.Retry)
    msgBox = QtWidgets.QMessageBox()
    msgBox.setWindowTitle(title)
    msgBox.setIcon(QtWidgets.QMessageBox.Critical)
    msgBox.setText(content)
    msgBox.addButton('確定', QtWidgets.QMessageBox.AcceptRole)
    # msgBox.setDefaultButton(QMessageBox.Retry)
    # msgBox.setDetailedText('这是详细的信息：学点编程吧，我爱你！')
    reply = msgBox.exec() 
    # if reply == QMessageBox.Retry:
    #     self.la.setText('你选择了Retry！') 
    # elif reply == QMessageBox.Abort:
    #     self.la.setText('你选择了Abort！')
    # else:
    #     self.la.setText('你选择了Ignore！')
