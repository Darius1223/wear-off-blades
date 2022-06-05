from typing import Callable

from PyQt5.QtWidgets import QMessageBox

from utils.messages import show_dialog


def catch_handle(func: Callable):
    """
    Утилита, в случае ошибки в функции выводит message_box
    :param func:
    :return: None
    """

    def wrapper(*args) -> None:
        try:
            func(args[0])
        except Exception as exc:
            show_dialog(
                title=f"{exc.__class__}",
                body=str(exc),
                msg_type=QMessageBox.Warning,
            )

    return wrapper
