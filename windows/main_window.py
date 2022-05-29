from PyQt5 import QtGui
from PyQt5.QtGui import QDoubleValidator, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QMessageBox

import texts
from entities import WearData
from templates.wear_of_blades import Ui_WearOfBlades
from utils.handles import catch_handle
from utils.messages import show_dialog
from windows import PlotWindow


class MainWindow(QMainWindow, Ui_WearOfBlades):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.data = WearData()
        self._init_ui()

    def _init_ui(self):
        self.setWindowIcon(QtGui.QIcon("images/icon1.ico"))
        self.plot_window = PlotWindow()
        self.start_plot_push_button.clicked.connect(self._start_plot_event)
        # Actions
        self.about_action.setShortcut(QKeySequence("F1"))
        self.about_action.triggered.connect(
            (
                lambda: show_dialog(
                    title="О программе",
                    body=texts.ABOUT_TEXT,
                    msg_type=QMessageBox.Information,
                    info="Все права защищены.",
                )
            )
        )
        self.authors_action.triggered.connect(
            (
                lambda: show_dialog(
                    title="Авторы",
                    body=texts.AUTHORS_TEXT,
                    msg_type=QMessageBox.Information,
                    info="Спасибо за пользование нашей программой!",
                )
            )
        )

        self.authors_action.setShortcut(QKeySequence("F2"))
        # Events
        section_events = [
            {
                "fields": [
                    (self.beforeTestLineEdit, "До испытаний", "before_test"),
                    (self.afterTestLineEdit, "После испытаний", "after_test"),
                ],
                "calculate": self.data.calculate_wear,
                "result_field": self.wearLineEdit,
                "button": self.calculateWearPushButton,
            },
            {
                "fields": [
                    (self.radiusLineEdit, "Радиус затупления", "radius"),
                    (self.widthLineEdit, "Толщина", "width"),
                ],
                "calculate": self.data.calculate_blunting,
                "result_field": self.bluntingLineEdit,
                "button": self.calculateBluntingPushButton,
            },
            {
                "fields": [
                    (self.frequencLineEdit, "Частота вращения ножа", "frequency"),
                    (self.timeTestLineEdit, "Время испытания", "time_test"),
                    (self.beforeTestLineEdit2, "До испытаний", "before_test"),
                    (self.afterTestLineEdit2, "После испытаний", "after_test"),
                ],
                "calculate": self.data.calculate_operating_time,
                "result_field": self.operatingTimeLneEdit,
                "button": self.calculateOperatingTimePushButton,
            },
            {
                "fields": [
                    (self.operatingTimeLneEdit3, "Предельная наработка", "operating_time"),
                    (self.maxSpeedLineEdit, "Макс. скорость резанья", "max_speed"),
                ],
                "calculate": self.data.calculate_resource,
                "result_field": self.resourceLineEdit,
                "button": self.calculateResourcePushButton,
            },
            {
                "fields": [
                    (self.operatingTimeLneEdit_2, "Предельная наработка", "operating_time"),
                    (self.timeTestLineEdit2, "Время испытания ножа", "time_test"),
                    (self.maxSpeedLineEdit2, "Макс. скорость резанья", "max_speed"),
                ],
                "calculate": self.data.calculate_ratio,
                "result_field": self.ratioLineEdit,
                "button": self.calculateRatioPushButton,
            },
        ]
        for section_event in section_events:
            section_event["button"].clicked.connect(
                self.calculate_event(
                    fields=section_event["fields"],
                    calculate=section_event["calculate"],
                    result_field=section_event["result_field"],
                )
            )

        # Validators
        validator = QDoubleValidator()
        line_edits = [
            self.beforeTestLineEdit,
            self.afterTestLineEdit,
            self.beforeTestLineEdit2,
            self.afterTestLineEdit2,
            self.radiusLineEdit,
            self.bluntingLineEdit,
            self.timeTestLineEdit,
            self.timeTestLineEdit2,
            self.operatingTimeLneEdit,
            self.frequencLineEdit,
            self.widthLineEdit,
        ]
        for line_edit in line_edits:
            line_edit.setValidator(validator)

        # Twins
        twins = [
            (self.beforeTestLineEdit, self.beforeTestLineEdit2),
            (self.afterTestLineEdit, self.afterTestLineEdit2),
            (self.timeTestLineEdit, self.timeTestLineEdit2),
            (self.operatingTimeLneEdit, self.operatingTimeLneEdit_2),
            (self.operatingTimeLneEdit, self.operatingTimeLneEdit3),
            (self.maxSpeedLineEdit, self.maxSpeedLineEdit2),
        ]
        for first, second in twins:
            self.update_twin_items(first, second)

    def calculate_event(self, fields, calculate, result_field):
        @catch_handle
        def _calculate_wear_event(*args, **kwargs):  # noqa
            for field in fields:
                line_edit, field_name, attr_name = field
                value = self.get_integer(line_edit, field_name)
                self.data.__setattr__(attr_name, value)
            try:
                value = calculate()
            except ZeroDivisionError:
                raise ZeroDivisionError("На 0 делить нельзя.")
            result_field.setText(str(value))

        return _calculate_wear_event

    @catch_handle
    def _calculate_blunting_event(self):
        self.data.before_test = self.get_integer(self.beforeTestLineEdit, "До испытаний")
        self.data.after_test = self.get_integer(self.afterTestLineEdit, "После испытаний")
        self.data.calculate_blunting()
        self.wearLineEdit.setText(str(self.data.wear))

    def update_twin_items(self, first: QLineEdit, second: QLineEdit):  # noqa
        def update(e):
            second.setText(e)

        first.textChanged.connect(update)  # noqa

    def get_integer(self, item: QLineEdit, field_name: str):  # noqa
        if item.text():
            return float(item.text().replace(",", "."))
        raise ValueError(f"Поле '{field_name}' должно быть заполнено")

    def _start_plot_event(self):
        self.plot_window.show()
