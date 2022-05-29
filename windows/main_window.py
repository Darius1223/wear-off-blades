from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from templates.wear_of_blades import Ui_WearOfBlades
from windows import PlotWindow


class MainWindow(QMainWindow, Ui_WearOfBlades):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self._init_ui()

    def _init_ui(self):
        self.setWindowIcon(QtGui.QIcon("images/icon1.ico"))
        self.plot_window = PlotWindow()
        self.start_plot_push_button.clicked.connect(self._start_plot_event)

    def _start_plot_event(self):
        self.plot_window.show()
