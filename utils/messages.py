from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


def show_dialog(title: str, body: str, msg_type: int, info=None):
    msg = QMessageBox()
    msg.setIcon(msg_type)
    msg.setWindowIcon(QIcon("images/warning.ico"))
    msg.setText(body)
    msg.setInformativeText(info or "Исправьте значения и повторите еще раз.")
    msg.setWindowTitle(title)
    msg.exec_()
