import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader


class Tic_Tac_Toe(QMainWindow):
    def __init__(self):
        # Properties
        loader = QUiLoader()
        self.main_window = loader.load("tic_tac_toe.ui")
        self.main_window.show()

        self.mode = None
        self.player = 1
        self.sign = "X"
        self.draw = 0
        self.your_score = 0
        self.opponent_score = 0
        self.buttons = [[self.main_window.btn_1, self.main_window.btn_2, self.main_window.btn_3],
                        [self.main_window.btn_4, self.main_window.btn_5, self.main_window.btn_6],
                        [self.main_window.btn_7, self.main_window.btn_8, self.main_window.btn_9]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))

        #self.main_window.btn_new_game.clicked.connect()
        #self.main_window.btn_about.clicked.connect()
        self.main_window.rb_cpu.toggled.connect(self.type_of_game)
        self.main_window.rb_player_2.toggled.connect(self.type_of_game)
             
    # Methods
    def type_of_game(self):
        self.main_window.lbl_x.setText(f"X (YOU)\n{self.your_score}")
        self.main_window.lbl_draw.setText(f"DRAW\n{self.draw}")
        if self.main_window.rb_cpu.isChecked():
            self.main_window.lbl_o.setText(f"O (CPU)\n{self.opponent_score}")
            self.mode = "CPU"
        else:
            self.main_window.lbl_o.setText(f"O (PLAYER)\n{self.opponent_score}")
            self.mode = "Player"

    def play(self, row, col):
        if self.buttons[row][col].text() == "":
            if self.player == 1:
                self.buttons[row][col].setText(self.sign)
                self.buttons[row][col].setStyleSheet("color: #2CC6BC; background-color: #1F3540; border-radius: 5px;")
                self.check()
                self.player = 2
                self.sign = "O"
                if self.mode == "CPU":
                    self.play(random.randint(0, 2), random.randint(0, 2))
            else:
                self.buttons[row][col].setText(self.sign)
                self.buttons[row][col].setStyleSheet("color: #F0B430; background-color: #1F3540; border-radius: 5px;")
                self.check()
                self.player = 1
                self.sign = "X"

    def check(self):
        if self.check_win() == True:
            if self.sign == "X":
                message_box = QMessageBox(text="Congratulations to you 🎉")
                message_box.exec()
            else:
                message_box = QMessageBox(text="Congratulations to Player 2 🎉")
                message_box.exec()
        
        else:
            if self.check_draw() == True:
                message_box = QMessageBox(text="Both of you are equal!")
                message_box.exec()
               
    def check_win(self):
        win_checker = False
        for i in range(3):
            if (self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() == self.sign) or (self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() == self.sign):
                win_checker = True
                break
        if (self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() == self.sign) or (self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() == self.sign):
            win_checker = True
        return win_checker

    def check_draw(self):
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                if self.buttons[i][j].text() == "":
                    return False
        else:
            return True
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Tic_Tac_Toe()
    app.exec()