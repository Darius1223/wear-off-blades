from PyQt5 import QtGui
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMainWindow, QLineEdit

from entities import WearData
from templates.wear_of_blades import Ui_WearOfBlades
from utils.handles import catch_handle
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
            self.radiusLineEdit,
            self.bluntingLineEdit,
        ]
        for line_edit in line_edits:
            line_edit.setValidator(validator)

        # Twins
        self.beforeTestLineEdit.textChanged.connect(self.update_before_twin_items)
        self.afterTestLineEdit.textChanged.connect(self.update_after_twin_items)

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
        self.data.before_test = self.get_integer(
            self.beforeTestLineEdit, "До испытаний"
        )
        self.data.after_test = self.get_integer(
            self.afterTestLineEdit, "После испытаний"
        )
        self.data.calculate_blunting()
        self.wearLineEdit.setText(str(self.data.wear))

    def update_before_twin_items(self, e):
        self.beforeTestLineEdit2.setText(e)

    def update_after_twin_items(self, e):
        self.afterTestLineEdit2.setText(e)

    def get_integer(self, item: QLineEdit, field_name: str):  # noqa
        if item.text():
            return float(item.text().replace(",", "."))
        raise ValueError(f"Поле '{field_name}' должно быть заполнено")

    def _start_plot_event(self):
        self.plot_window.show()
