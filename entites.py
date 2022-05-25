from typing import Tuple, List

import settings


class PlotData:
    def __init__(self):
        self.current_row_index: int = 0
        self.row_count: int = settings.DEFAULT_ROW_COUNT
        self.data: List[Tuple[int, int]] = [settings.DEFAULT_DATA]

    @property
    def current_plot(self):
        return self.data[self.current_row_index]