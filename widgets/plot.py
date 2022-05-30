from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
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

    def avg_plot(self):
        self.figure.clear()
        x, y = self.plot_data.avg_data

        ax: Axes = self.figure.add_subplot()
        ax.set_title("Средний график износа ножа")
        ax.set_xlabel("Время, мин")
        ax.set_ylabel("Износ ножа, мм")

        ax.plot(
            x,
            y,
            "*-",
            label="Средний график",
        )
        ax.minorticks_on()
        ax.grid(which="major")
        ax.legend(fontsize=10)
        self.canvas.draw()

    def plot(self):
        self.figure.clear()

        ax: Axes = self.figure.add_subplot()
        ax.set_title("График износа ножа")
        ax.set_xlabel("Время, мин")
        ax.set_ylabel("Износ ножа, мм")
        for ind, _ in enumerate(self.plot_data.data):
            ax.plot(
                self.plot_data.x_data(ind),
                self.plot_data.y_data(ind),
                "*-",
                label=f"График #{ind + 1}",
            )
        ax.minorticks_on()
        ax.grid(which="major")
        ax.legend(fontsize=10)
        self.canvas.draw()
