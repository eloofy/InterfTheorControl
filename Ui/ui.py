from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from workLogic.logic_in import FunctionalityHandler

import matplotlib.pyplot as plt


class UiMainWindow(object):
    def __init__(self, main_window):
        self.main_window = main_window

        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.tableData = QtWidgets.QTableWidget(self.central_widget)
        self.GraphicChooseObj = QtWidgets.QComboBox(self.central_widget)
        self.WidjetViewGraphics = QtWidgets.QWidget(self.central_widget)
        self.pushButton_drawGraphic = QtWidgets.QPushButton(self.central_widget)
        self.pushButton_calculateTabl = QtWidgets.QPushButton(self.central_widget)
        self.LabelApp = QtWidgets.QLabel(self.central_widget)
        self.k_data = QtWidgets.QLineEdit(self.central_widget)
        self.t_data_2 = QtWidgets.QLineEdit(self.central_widget)
        self.eps_data = QtWidgets.QLineEdit(self.central_widget)
        self.t_data = QtWidgets.QLabel(self.central_widget)
        self.eps = QtWidgets.QLabel(self.central_widget)
        self.k = QtWidgets.QLabel(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(self.main_window)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)

        self.figure, self.ax = plt.subplots(figsize=(8, 6), dpi=100, constrained_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.WidjetViewGraphics)
        self.functionality_handler = FunctionalityHandler(ui_main_window=self)

        self.setup_ui()
        self.retranslate_ui()
        self.set_connections()

    def setup_ui(self):
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(732, 613)
        self.main_window.setMinimumSize(QtCore.QSize(0, 613))
        self.main_window.setMaximumSize(QtCore.QSize(732, 613))

        self.central_widget.setObjectName("centralwidget")
        self.tableData.setGeometry(QtCore.QRect(10, 400, 721, 161))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(10)
        size_policy.setVerticalStretch(10)
        size_policy.setHeightForWidth(self.tableData.sizePolicy().hasHeightForWidth())

        self.tableData.setSizePolicy(size_policy)
        self.tableData.setLineWidth(1)
        self.tableData.setAutoScrollMargin(2)
        self.tableData.setIconSize(QtCore.QSize(0, 0))
        self.tableData.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableData.setObjectName("tableData")
        self.tableData.setColumnCount(7)
        self.tableData.setRowCount(4)

        item = QtWidgets.QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()

        self.tableData.setHorizontalHeaderItem(6, item)
        self.tableData.horizontalHeader().setMinimumSectionSize(50)

        self.GraphicChooseObj.setGeometry(QtCore.QRect(10, 270, 291, 25))
        self.GraphicChooseObj.setObjectName("GraphicChooseObj")
        self.GraphicChooseObj.addItem("")
        self.GraphicChooseObj.addItem("")
        self.GraphicChooseObj.addItem("")
        self.GraphicChooseObj.addItem("")
        self.GraphicChooseObj.addItem("")
        self.GraphicChooseObj.addItem("")
        self.GraphicChooseObj.addItem("")
        self.GraphicChooseObj.addItem("")
        self.GraphicChooseObj.setItemText(7, "")

        self.WidjetViewGraphics.setGeometry(QtCore.QRect(310, 10, 411, 381))
        self.WidjetViewGraphics.setObjectName("WidjetViewGraphics")

        self.pushButton_drawGraphic.setGeometry(QtCore.QRect(10, 304, 291, 41))
        self.pushButton_drawGraphic.setObjectName("pushButton_drawGraphic")
        self.pushButton_calculateTabl.setGeometry(QtCore.QRect(10, 350, 291, 41))
        self.pushButton_calculateTabl.setObjectName("pushButton_calculateTabl")

        self.LabelApp.setGeometry(QtCore.QRect(10, 10, 291, 41))
        self.LabelApp.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelApp.setObjectName("LabelApp")

        self.k_data.setGeometry(QtCore.QRect(140, 60, 81, 31))
        self.k_data.setObjectName("k_data")

        self.t_data_2.setGeometry(QtCore.QRect(140, 110, 81, 31))
        self.t_data_2.setObjectName("t_data_2")

        self.eps_data.setGeometry(QtCore.QRect(140, 160, 81, 31))
        self.eps_data.setObjectName("eps_data")

        self.t_data.setGeometry(QtCore.QRect(80, 110, 67, 31))
        self.t_data.setAlignment(QtCore.Qt.AlignCenter)
        self.t_data.setObjectName("t_data")

        self.eps.setGeometry(QtCore.QRect(80, 160, 67, 31))
        self.eps.setScaledContents(False)
        self.eps.setAlignment(QtCore.Qt.AlignCenter)
        self.eps.setObjectName("eps")

        self.k.setGeometry(QtCore.QRect(80, 60, 67, 31))
        self.k.setAlignment(QtCore.Qt.AlignCenter)
        self.k.setObjectName("k")

        self.main_window.setCentralWidget(self.central_widget)

        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 732, 22))
        self.menu_bar.setObjectName("menubar")
        self.main_window.setMenuBar(self.menu_bar)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableData.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "A(ω)"))
        item = self.tableData.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "∆t(ω)"))
        item = self.tableData.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "φ(ω)"))
        item = self.tableData.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "L(ω)"))
        item = self.tableData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0.01"))
        item = self.tableData.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "0.03"))
        item = self.tableData.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "0.1"))
        item = self.tableData.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "0.3"))
        item = self.tableData.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableData.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableData.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "10"))
        self.GraphicChooseObj.setItemText(0, _translate("MainWindow", "График φ для ω = 0.01 Гц"))
        self.GraphicChooseObj.setItemText(1, _translate("MainWindow", "График Ax для ω = 0.01 Гц"))
        self.GraphicChooseObj.setItemText(2, _translate("MainWindow", "График A(ω)"))
        self.GraphicChooseObj.setItemText(3, _translate("MainWindow", "График φ(ω)"))
        self.GraphicChooseObj.setItemText(4, _translate("MainWindow", "График ЛАЧХ"))
        self.GraphicChooseObj.setItemText(5, _translate("MainWindow", "График ЛАЧХ и ЛФЧХ"))
        self.GraphicChooseObj.setItemText(6, _translate("MainWindow", "Годограф АФЧХ"))
        self.pushButton_drawGraphic.setText(_translate("MainWindow", "Draw graphic"))
        self.pushButton_calculateTabl.setText(_translate("MainWindow", " Calculate table"))
        self.LabelApp.setText(_translate("MainWindow", "Параметры динамических звеньев"))
        self.t_data.setText(_translate("MainWindow", "T="))
        self.eps.setText(_translate("MainWindow", "ξ ="))
        self.k.setText(_translate("MainWindow", "k="))

        layout = QtWidgets.QVBoxLayout(self.WidjetViewGraphics)
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)

    def set_connections(self):
        self.pushButton_drawGraphic.clicked.connect(self.functionality_handler.draw_graphic)
        self.pushButton_calculateTabl.clicked.connect(self.functionality_handler.populate_table)
