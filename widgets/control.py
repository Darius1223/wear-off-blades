from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QWidget,
    QFormLayout,
    QSpinBox,
    QLabel,
    QComboBox,
    QPushButton,
)

from widgets import PlotWidget


class ControlWidget(QWidget):
    """Виджет управления графиками"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.table = self.parent().table_widget  # noqa
        self.plot_widget: PlotWidget = self.parent().plot_widget  # noqa
        self.plot_data = self.parent().plot_data  # noqa
        self._init_ui()

    def _init_ui(self):
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.setFont(font)

        self.formLayout = QFormLayout()
        self.setLayout(self.formLayout)

        # row count
        self.row_count_spin_box = QSpinBox()
        self.row_count_label = QLabel("Кол-во строк:")
        self.formLayout.insertRow(0, self.row_count_label, self.row_count_spin_box)
        self.row_count_spin_box.textChanged.connect(self._set_row_count_event)
        self.row_count_spin_box.setValue(self.table.rowCount())
        # plot count
        self.plot_count_spin_box = QSpinBox()
        self.plot_count_spin_box.setMinimum(1)
        self.plot_count_spin_box.setValue(self.plot_widget.plot_data.plot_count)
        self.plot_count_spin_box.valueChanged.connect(self._set_plot_count_event)
        self.plot_count_label = QLabel("Кол-во графиков:")
        self.formLayout.insertRow(1, self.plot_count_label, self.plot_count_spin_box)
        # choice plot
        self.dropdownLabel = QLabel("Выбрать график:")
        self.dropdownLabel.setFont(font)
        self.dropdown = QComboBox()
        self.dropdown.setFont(font)
        self.formLayout.insertRow(2, self.dropdownLabel, self.dropdown)
        self._update_ui()
        self.dropdown.currentIndexChanged.connect(self._choice_plot_event)
        # plot
        self.plot_label = QLabel("График:")
        self.plot_button = QPushButton("Построить")
        self.plot_button.clicked.connect(self._plot_event)
        self.formLayout.insertRow(3, self.plot_label, self.plot_button)
        # avg plot
        self.avg_plot_label = QLabel("Средний график:")
        self.avg_plot_button = QPushButton("Построить")
        self.avg_plot_button.clicked.connect(self._avg_plot_event)
        self.formLayout.insertRow(4, self.avg_plot_label, self.avg_plot_button)

    def _choice_plot_event(self, e):
        self.plot_data.current_plot_index = e
        self.table.update_ui()

    def _set_plot_count_event(self):
        value = self.plot_count_spin_box.value()
        self.plot_data.fill_plot(value)
        self.plot_data.plot_count = value
        self._update_ui()

    def _update_ui(self):
        self.dropdown.clear()
        for i in range(1, self.plot_data.plot_count + 1):
            self.dropdown.addItem(f"График №{i}", i)

    def _plot_event(self):
        self.plot_widget.plot()

    def _avg_plot_event(self):
        self.plot_widget.avg_plot()

    def _set_row_count_event(self):
        value = self.row_count_spin_box.value()
        self.table.update_row_count(value)
