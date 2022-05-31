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
        self.setWindowIcon(QtGui.QIcon(":/images/Icon1.ico"))
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
        # Далее: мегахак
        # Т.к. первое окно состоит из 5 похожых секций
        # я запилил список словарей для каждого из них, где
        # == fields: Tuple(источник_данных, его_название, куда_класть)
        # == calculate: функция вычисления результата
        # == result_field: куда класть результат
        # == button: кнопка-триггер которая запускает вычления
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
                self._calculate_event(
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
        # Второй мегахак:
        # В исходной проге были LineEdit - близнецы: заполняем первый -> заполняется второй
        # twins - список близнецов
        twins = [
            (self.beforeTestLineEdit, self.beforeTestLineEdit2),
            (self.afterTestLineEdit, self.afterTestLineEdit2),
            (self.timeTestLineEdit, self.timeTestLineEdit2),
            (self.operatingTimeLneEdit, self.operatingTimeLneEdit_2),
            (self.operatingTimeLneEdit, self.operatingTimeLneEdit3),
            (self.maxSpeedLineEdit, self.maxSpeedLineEdit2),
        ]
        for first, second in twins:
            self._update_twin_items(first, second)

    def _calculate_event(self, fields, calculate, result_field):
        """ Генерирование events-сигналов для секций """

        @catch_handle
        def _calculate_wear_event(*args, **kwargs):  # noqa
            for field in fields:
                line_edit, field_name, attr_name = field
                value = self._get_digit_from_item(line_edit, field_name)
                self.data.__setattr__(attr_name, value)
            try:
                value = calculate()
            except ZeroDivisionError:
                raise ZeroDivisionError("На 0 делить нельзя.")
            self.statusBar().showMessage(f"Результат: {value}", msecs=1000)
            result_field.setText(str(value))

        return _calculate_wear_event

    def _update_twin_items(self, first: QLineEdit, second: QLineEdit):  # noqa
        """ Генерирование events-сигналов для близнецов """

        def update(e):
            second.setText(e)

        first.textChanged.connect(update)  # noqa

    def _get_digit_from_item(self, item: QLineEdit, field_name: str):  # noqa
        if item.text():
            return float(item.text().replace(",", "."))
        raise ValueError(f"Поле '{field_name}' должно быть заполнено")

    def _start_plot_event(self):
        self.plot_window.show()
