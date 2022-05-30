from PyQt5.QtWidgets import QMessageBox
from loguru import logger

from utils.messages import show_dialog


def catch_handle(func):
    def f(*args):
        logger.info(f)
        logger.info(args)
        try:
            func(args[0])
        except Exception as exc:
            logger.error(f"{exc=}")
            show_dialog(
                title=f"{exc.__class__}",
                body=str(exc),
                msg_type=QMessageBox.Warning,
            )

    return f
