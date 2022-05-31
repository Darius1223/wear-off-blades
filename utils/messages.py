from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

DEFAULT_INFO = "Исправьте значения и повторите еще раз."


def show_dialog(
    title: str,
    body: str,
    msg_type: int,
    info=DEFAULT_INFO,
) -> None:
    """
    Вывод диалога на экран
    :param title:
    :param body:
    :param msg_type:
    :param info:
    :return:
    """

    message_box = QMessageBox()
    message_box.setIcon(msg_type)
    message_box.setWindowIcon(QIcon(":/images/warning.ico"))
    message_box.setText(body)
    message_box.setInformativeText(info)
    message_box.setWindowTitle(title)
    message_box.exec_()
