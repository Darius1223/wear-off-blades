import copy
from typing import List

import settings


class PlotData:
    def __init__(self):
        self.current_plot_index: int = 0
        self.row_count: int = settings.DEFAULT_ROW_COUNT
        self.plot_count: int = settings.DEFAULT_PLOT_COUNT
        self.data: List[List[List[int, int]]] = [settings.DEFAULT_DATA]

    @property
    def avg_data(self):
        all_x = set()

        for i in range(self.plot_count):
            all_x = all_x.union(set(self.x_data(i)))

        all_x = sorted(all_x)
        all_y = []

        for x in all_x:
            sum_y = 0
            count_y = 0
            for plot in self.data:
                for temp_x, temp_y in plot:
                    if temp_x == x:
                        sum_y += temp_y
                        count_y += 1
            all_y.append(sum_y / count_y)
        return all_x, all_y

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
                self.data.append(
                    [copy.copy(settings.DEFAULT_VECTOR) for _ in range(self.row_count)])
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
