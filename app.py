import sys
from typing import List, Tuple

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QTableWidget, QTableWidgetItem,
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

from matplotlib.figure import Figure

from control import Ui_Form
from entites import PlotData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # data
        self.plot_data = PlotData()

        self._init_ui()

    def _init_ui(self):
        font = QtGui.QFont()
        font.setPointSize(15)
        # central_widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # layout
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        # widgets
        self.plot_widget = PlotWidget()
        self.table_widget = PlotTable(self.plot_data)
        self.control_widget = ControlWidget(self.table_widget, self.plot_widget)
        # plot
        self.plot_label = QLabel("График")
        self.plot_label.setFont(font)
        # self.grid_layout.addWidget(self.plot_label, 2, 2)
        self.grid_layout.addWidget(self.plot_widget, 2, 0)
        # table
        self.table_label = QLabel("Таблица")
        self.table_label.setFont(font)
        self.grid_layout.addWidget(self.table_label, 0, 1)
        self.grid_layout.addWidget(self.table_widget, 1, 1, 2, 1)
        # control
        self.control_label = QLabel("Панель управленмя")
        self.control_label.setFont(font)
        self.grid_layout.addWidget(self.control_label, 0, 0)
        self.grid_layout.addWidget(self.control_widget, 1, 0)

    def _update_ui(self):
        self.table_widget.update_ui()


class PlotTable(QTableWidget):
    """Виджет для отображения таблицы значений"""

    def __init__(self, plot_data: PlotData):
        super().__init__()
        self.plot_data = plot_data
        self._init_ui()

    def _init_ui(self):
        self.setHorizontalHeaderLabels(("X", "Y"))
        self.setColumnCount(2)
        self.update_ui()

    def update_ui(self):
        self.setRowCount(self.plot_data.row_count)
        for ind_row, vector in enumerate(self.plot_data.current_plot):
            x, y = vector
            self.setItem(ind_row, 0, QTableWidgetItem(str(x)))
            self.setItem(ind_row, 1, QTableWidgetItem(str(y)))


class ControlWidget(QWidget, Ui_Form):
    """ Виджет управления графиками """

    def __init__(self, table: PlotTable, plot_widget: "PlotWidget"):
        super().__init__()
        self.table = table
        self.plot_widget = plot_widget
        self.setupUi(self)
        self._init_ui()

    def _init_ui(self):
        self.row_count_button.clicked.connect(self._set_row_count_event)
        self.row_count_spin_box.setValue(self.table.rowCount())
        self.plot_button.clicked.connect(self.plot_widget.plot)

    def _set_row_count_event(self):
        value = self.row_count_spin_box.value()
        self.table.setRowCount(value)


class PlotWidget(QWidget):
    """Виджет для отображения графика"""

    def __init__(self):
        super().__init__()
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
        data = [random.random() for i in range(10)]

        colors = "bgrcmk"
        ax = self.figure.add_subplot(111)
        ax.plot(data, random.choice(colors))
        ax.plot([random.random() for i in range(10)], random.choice(colors))
        # self.figure.clear()
        # ax = self.figure.add_subplot(111)
        # az = self.figure.add_subplot(111)
        # # ax = self.figure.add_subplot(111)
        # # ay = self.figure.add_subplot(111)
        # ax.plot(data, [random.randint(1, 10) for i in range(10)])
        # az.plot(data, [random.randint(1, 10) for i in range(10)])
        # # ay.plot(data, "*-")
        #
        # # refresh canvas
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    app.exec()
