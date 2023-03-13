import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_main_window

class MainWindow(QMainWindow):
    def __init__(self):
        # Properties
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)