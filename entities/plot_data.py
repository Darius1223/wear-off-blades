import copy
from typing import List

import settings


class PlotData:
    def __init__(self):
        self.current_plot_index: int = 0
        self.row_count: int = settings.DEFAULT_ROW_COUNT
        self.plot_count: int = settings.DEFAULT_PLOT_COUNT
        self.data: List[List[List[int, int]]] = [settings.DEFAULT_DATA]

    def fill_rows(self, new_count: int) -> None:
        dist = new_count - self.row_count
        for ind_plot, _ in enumerate(self.data):
            for _ in range(abs(dist)):
                if dist > 0:
                    self.data[ind_plot].append(copy.copy(settings.DEFAULT_VECTOR))
                else:
                    self.data[ind_plot].pop()

    def fill_plot(self, new_count: int) -> None:
        dist = new_count - self.plot_count
        for _ in range(abs(dist)):
            if dist > 0:
                self.data.append([copy.copy(settings.DEFAULT_VECTOR) for _ in range(self.row_count)])
            else:
                self.data.pop()

    @property
    def current_plot(self):
        return self.data[self.current_plot_index]

    @current_plot.setter
    def current_plot(self, value):
        self.data[self.current_plot_index] = list(value)

    def x_data(self, ind):
        return [vector[0] for vector in self.data[ind]]

    def y_data(self, ind):
        return [vector[1] for vector in self.data[ind]]
