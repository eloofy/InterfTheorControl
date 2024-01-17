from PyQt5 import QtWidgets
import numpy as np
from Config.cfg import PLOTS

from workLogic.logic import Model


class FunctionalityHandler:
    def __init__(self, ui_main_window):
        self.ui_main_window = ui_main_window
        self.model = None

    def draw_graphic(self):
        selected_option = self.ui_main_window.GraphicChooseObj.currentText()

        try:
            if selected_option in PLOTS:
                self.ui_main_window.figure.clear()
                PLOTS[selected_option](self.model, ui=self)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ui_main_window.main_window, "Error", "Do the calculations before you draw.")
            return

    def populate_table(self):
        try:
            k_value = float(self.ui_main_window.k_data.text())
            t_value = float(self.ui_main_window.t_data_2.text())
            eps_value = float(self.ui_main_window.eps_data.text())
        except ValueError:
            QtWidgets.QMessageBox.critical(self.ui_main_window.main_window, "Error", "Enter the initial data.")
            return
        self.model = Model(k_value,
                           t_value,
                           eps_value)
        self.model.init()

        for row in range(self.ui_main_window.tableData.rowCount()):
            for col in range(self.ui_main_window.tableData.columnCount()):
                item = QtWidgets.QTableWidgetItem(str(round(self.model.table_data[row, col], 5)))
                self.ui_main_window.tableData.setItem(row, col, item)

        header = self.ui_main_window.tableData.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

        for col in range(self.ui_main_window.tableData.columnCount()):
            header.resizeSection(col, 96)

    def get_table_column_values(self, column_index):
        values = []
        for col in range(self.ui_main_window.tableData.columnCount()):
            item = self.ui_main_window.tableData.item(column_index, col)
            if item is not None:
                values.append(float(item.text()))
        return values
