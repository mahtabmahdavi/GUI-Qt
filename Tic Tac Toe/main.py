import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader


class Tic_Tac_Toe(QMainWindow):
    def __init__(self):
        # Properties
        loader = QUiLoader()
        self.main_window = loader.load("tic_tac_toe.ui")
        self.main_window.show()

        self.player = 1
        self.buttons = [[self.main_window.btn_1, self.main_window.btn_2, self.main_window.btn_3],
                        [self.main_window.btn_4, self.main_window.btn_5, self.main_window.btn_6],
                        [self.main_window.btn_7, self.main_window.btn_8, self.main_window.btn_9]]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
        
    # Methods
    def play(self, row, col):
        if self.player == 1:
            self.buttons[row][col].setText("X")
            self.player = 2
        else:
            self.buttons[row][col].setText("O")
            self.player = 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Tic_Tac_Toe()
    app.exec()