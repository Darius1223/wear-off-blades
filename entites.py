from typing import Tuple, List

import settings


class PlotData:
    def __init__(self):
        self.current_row_index: int = 0
        self.row_count: int = settings.DEFAULT_ROW_COUNT
        self.data: List[List[Tuple[int, int]]] = [settings.DEFAULT_DATA]

    @property
    def current_plot(self):
        return self.data[self.current_row_index]

    @current_plot.setter
    def current_plot(self, value):
        self.data[self.current_row_index] = list(value)

    @property
    def x_data(self):
        return [vector[0] for vector in self.current_plot]

    @property
    def y_data(self):
        return [vector[1] for vector in self.current_plot]
