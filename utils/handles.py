from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from loguru import logger


def catch_handle(func):
    def f(*args):
        logger.info(f)
        logger.info(args)
        try:
            func(args[0])
        except Exception as exc:
            logger.error(f"{exc=}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowIcon(QIcon("images/warning.ico"))
            msg.setText(str(exc))
            msg.setInformativeText("Исправьте значения и повторите еще раз.")
            msg.setWindowTitle(f"{exc.__class__}")
            msg.exec_()

    return f
