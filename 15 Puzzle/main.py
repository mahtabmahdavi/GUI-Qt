import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from functions import generate_non_repeating_random_numbers_2d_list


class MainWindow(QMainWindow):
    def __init__(self):
        # Properties
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
                        [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
                        [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
                        [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]]
        
        random_numbers = generate_non_repeating_random_numbers_2d_list(4, 4)
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].setText(str(random_numbers[i][j]))
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                if random_numbers[i][j] == 16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_row = i
                    self.empty_col = j

    # Methods
    def play(self, row, col):
        if (row == self.empty_row and abs(col - self.empty_col) == 1) or (col == self.empty_col and abs(row - self.empty_row) == 1):
            self.buttons[self.empty_row][self.empty_col].setText(self.buttons[row][col].text())
            self.buttons[row][col].setText("16")
            self.buttons[self.empty_row][self.empty_col].setVisible(True)
            self.buttons[row][col].setVisible(False)
            self.empty_row = row
            self.empty_col = col
        if self.check_win() == True:
            message_box = QMessageBox()
            message_box.setWindowTitle("Congratulations")
            message_box.setText("You win the game 🥳        ")
            message_box.exec()

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True
                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()