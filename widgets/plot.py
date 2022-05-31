from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.axes._subplots import Axes  # noqa

from entities import PlotData


class PlotWidget(QWidget):
    """Виджет для отображения графика"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.plot_data: PlotData = self.parent().plot_data  # noqa
        self._init_ui()

    def _init_ui(self):
        self.figure: Figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        # plot_buttons
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_event)
        # set the layout
        self.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        # data
        self.plot_style = "*-"

    def avg_plot_event(self):
        self.figure.clear()

        x_data, y_data = self.plot_data.avg_data
        ax: Axes = self.figure.add_subplot()
        ax.set_title("Средний график износа ножа")
        ax.set_xlabel("Время, мин")
        ax.set_ylabel("Износ ножа, мм")

        ax.plot(x_data, y_data, self.plot_style, label="Средний график")
        ax.minorticks_on()
        ax.grid(which="major")
        ax.legend(fontsize=10)
        self.canvas.draw()

    def plot_event(self):
        self.figure.clear()

        ax: Axes = self.figure.add_subplot()
        ax.set_title("График износа ножа")
        ax.set_xlabel("Время, мин")
        ax.set_ylabel("Износ ножа, мм")
        for ind, _ in enumerate(self.plot_data.data):
            x_data, y_data = self.plot_data.x_data(ind), self.plot_data.y_data(ind)
            ax.plot(x_data, y_data, self.plot_style, label=f"График #{ind + 1}")
        ax.minorticks_on()
        ax.grid(which="major")
        ax.legend(fontsize=10)
        self.canvas.draw()
