from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class TableWidget(QTableWidget):
    """Виджет для отображения таблицы значений"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.plot_data = self.parent().plot_data  # noqa
        self._init_ui()

    def _init_ui(self):
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(['Время, сек', 'Износ ножа, мм'])
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
