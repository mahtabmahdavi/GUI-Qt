import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader


class Tic_Tac_Toe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.main_window = loader.load("tic_tac_toe.ui")
        self.main_window.show()
        # Properties
        self.sign = "X"
        self.tie = 0
        self.cpu_score = 0
        self.player_1_score = 0
        self.player_2_score = 0
        self.buttons = [[self.main_window.btn_1, self.main_window.btn_2, self.main_window.btn_3],
                        [self.main_window.btn_4, self.main_window.btn_5, self.main_window.btn_6],
                        [self.main_window.btn_7, self.main_window.btn_8, self.main_window.btn_9]]
        self.main_window.rb_cpu.setChecked(True)
        self.game_type()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
        self.main_window.btn_new_game.clicked.connect(self.reset_game)
        self.main_window.btn_about.clicked.connect(self.show_about)
        self.main_window.rb_cpu.toggled.connect(self.game_type)
        self.main_window.rb_player_2.toggled.connect(self.game_type)
             
    # Methods
    def game_type(self):
        self.sign = "X"
        self.tie = 0
        self.cpu_score = 0
        self.player_1_score = 0
        self.player_2_score = 0
        self.reset_game()
        if self.main_window.rb_cpu.isChecked():
            self.mode = "CPU"
        elif self.main_window.rb_player_2.isChecked():
            self.mode = "Player"
        self.show_turn()
        self.show_score()
    
    def show_turn(self):
        if self.sign == "X":
            self.main_window.lbl_turn.setText(f"{self.sign} TURN")
        else:
            self.main_window.lbl_turn.setText(f"{self.sign} TURN")
    
    def show_score(self):
        self.main_window.lbl_x.setText(f"X (YOU)\n{self.player_1_score}")
        self.main_window.lbl_tie.setText(f"TIE\n{self.tie}")
        if self.mode == "CPU":
            self.main_window.lbl_o.setText(f"O (CPU)\n{self.cpu_score}")
        elif self.mode == "Player":
            self.main_window.lbl_o.setText(f"O (PLAYER)\n{self.player_2_score}")

    def play(self, row, col):
        if self.buttons[row][col].text() == "":
            if self.sign == "X":
                self.buttons[row][col].setText(self.sign)
                self.buttons[row][col].setStyleSheet("color: #2CC6BC; background-color: #1F3540; border-radius: 5px;")
                self.check_game()
                self.sign = "O"
                self.show_turn()
                if self.mode == "CPU":
                    temp_row = random.randint(0, 2)
                    temp_col = random.randint(0, 2)
                    while self.buttons[temp_row][temp_col].text() != "":
                        temp_row = random.randint(0, 2)
                        temp_col = random.randint(0, 2)
                    self.play(temp_row, temp_col) 
            else:
                self.buttons[row][col].setText(self.sign)
                self.buttons[row][col].setStyleSheet("color: #F0B430; background-color: #1F3540; border-radius: 5px;")
                self.check_game()
                self.sign = "X"
                self.show_turn()

    def check_game(self):
        if self.check_win() == True:
            message_box = QMessageBox()
            message_box.setWindowTitle("Congratulations")
            if self.sign == "X":
                self.player_1_score += 1
                self.show_score()
                if self.mode == "CPU":
                    message_box.setText("You win the game 🥂        ")
                else:
                    message_box.setText("Player 1 wins the game 🎉      ")
            else:
                if self.mode == "CPU":
                    self.cpu_score += 1
                    self.show_score()
                    message_box.setText("Computer wins the game 🙄      ")
                else:
                    self.player_2_score += 1
                    self.show_score()
                    message_box.setText("Player 2 wins the game 🎉     ")
            message_box.exec()
            self.reset_game()
        else:
            if self.check_tie() == True:
                self.tie += 1
                self.show_score()
                message_box = QMessageBox(text = "Both of you are equal 🤝      ")
                message_box.setWindowTitle("Tie")
                message_box.exec()
                if self.mode == "CPU":
                    self.reset_game()
     
    def check_win(self):
        win_checker = False
        for i in range(3):
            if (self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() == self.sign) or (self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() == self.sign):
                win_checker = True
                break
        if (self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() == self.sign) or (self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() == self.sign):
            win_checker = True
        return win_checker

    def check_tie(self):
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                if self.buttons[i][j].text() == "":
                    return False
        else:
            return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText("")

    def show_about(self):
        message_box = QMessageBox(text = """  Tic Tac Toe is a simple game for two players.
The first player who can quickly fill a row or a column or diagonally
a 3 x 3 square wins the game. If all the cells of the table are filled
and no one succeeds in completing the mentioned conditions,
the game will be tied.""")
        message_box.setWindowTitle("About")
        message_box.exec()

# -------------------- End of Game Class -------------------- #

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Tic_Tac_Toe()
    app.exec()