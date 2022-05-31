import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
)

from entities import PlotData
from widgets import PlotWidget, ControlWidget, TableWidget


class PlotWindow(QMainWindow):
    """Окно построения графика"""

    def __init__(self):
        super().__init__()
        self.plot_data = PlotData()  # data

        self._init_ui()

    def _init_ui(self):
        self.setWindowIcon(QtGui.QIcon("images/icon1.ico"))
        # self.resize(900, 650)
        # self.setMinimumSize(QSize(900, 650))
        # self.setMaximumSize(QSize(900, 650))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.setWindowTitle("Построение графика")
        # central_widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # layout
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        # widgets
        self.plot_widget = PlotWidget(self)
        self.table_widget = TableWidget(self)
        self.control_widget = ControlWidget(self)
        # plot
        self.plot_label = QLabel("График")
        self.plot_label.setFont(font)
        self.grid_layout.addWidget(self.plot_widget, 2, 0)
        # table
        self.table_label = QLabel("Таблица")
        self.table_label.setFont(font)
        self.table_label.setFixedHeight(20)
        self.grid_layout.addWidget(self.table_label, 0, 1)
        self.grid_layout.addWidget(self.table_widget, 1, 1, 2, 1)
        # control
        self.control_label = QLabel("Панель управления")
        self.control_label.setFont(font)
        self.control_label.setFixedHeight(20)
        self.grid_layout.addWidget(self.control_label, 0, 0)
        self.grid_layout.addWidget(self.control_widget, 1, 0)

    def _update_ui(self):
        self.table_widget.update_ui()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = PlotWindow()
    main.show()

    app.exec()
