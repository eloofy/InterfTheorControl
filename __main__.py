from PyQt5 import QtWidgets
from Ui.ui import UiMainWindow
import sys


def run_application():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_application()