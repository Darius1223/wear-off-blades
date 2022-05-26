import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QFormLayout,
    QSpinBox,
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

from matplotlib.figure import Figure

from entites import PlotData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.plot_data = PlotData()  # data

        self._init_ui()

    def _init_ui(self):
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setWindowTitle("Построение графика")
        # central_widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # layout
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        # widgets
        self.plot_widget = PlotWidget(self)
        self.table_widget = PlotTable(self)
        self.control_widget = ControlWidget(self)
        # plot
        self.plot_label = QLabel("График")
        self.plot_label.setFont(font)
        self.grid_layout.addWidget(self.plot_widget, 2, 0)
        # table
        self.table_label = QLabel("Таблица")
        self.table_label.setFont(font)
        self.grid_layout.addWidget(self.table_label, 0, 1)
        self.grid_layout.addWidget(self.table_widget, 1, 1, 2, 1)
        # control
        self.control_label = QLabel("Панель управления")
        self.control_label.setFont(font)
        self.grid_layout.addWidget(self.control_label, 0, 0)
        self.grid_layout.addWidget(self.control_widget, 1, 0)

    def _update_ui(self):
        self.table_widget.update_ui()


class PlotTable(QTableWidget):
    """Виджет для отображения таблицы значений"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.plot_data = self.parent().plot_data  # noqa
        self._init_ui()

    def _init_ui(self):
        self.setHorizontalHeaderLabels(("X", "Y"))
        self.setColumnCount(2)
        self.setFixedWidth(225)
        self.cellChanged.connect(self._update_data_by_table)
        self.update_ui()

    def _update_data_by_table(self, row, col):
        new_value = int(self.item(row, col).text())
        self.plot_data.data[self.plot_data.current_plot_index][row][col] = new_value

    def update_row_count(self, value: int):
        self.plot_data.fill_rows(value)
        self.plot_data.row_count = value
        self.setRowCount(value)
        self.update_ui()

    def update_ui(self):
        self.setRowCount(self.plot_data.row_count)
        for ind_row, vector in enumerate(self.plot_data.current_plot):
            x, y = vector
            self.setItem(ind_row, 0, QTableWidgetItem(str(x)))
            self.setItem(ind_row, 1, QTableWidgetItem(str(y)))


class ControlWidget(QWidget):
    """Виджет управления графиками"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.table = self.parent().table_widget  # noqa
        self.plot_widget = self.parent().plot_widget  # noqa
        self.plot_data = self.parent().plot_data  # noqa
        self._init_ui()

    def _init_ui(self):
        font = QtGui.QFont()
        font.setPointSize(15)
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
        # self.plot_button.clicked.connect(self._plot_event)
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

    def _set_row_count_event(self):
        value = self.row_count_spin_box.value()
        self.table.update_row_count(value)


class PlotWidget(QWidget):
    """Виджет для отображения графика"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.plot_data = self.parent().plot_data  # noqa

        self.figure: Figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QPushButton("Plot")
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):
        self.figure.clear()

        colors = "bgrcmk"
        ax = self.figure.add_subplot(111)
        for ind, _ in enumerate(self.plot_data.data):
            ax.plot(
                self.plot_data.x_data(ind),
                self.plot_data.y_data(ind),
                c=random.choice(colors),
            )

        # # ay.plot(data, "*-")
        # # refresh canvas
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    app.exec()
