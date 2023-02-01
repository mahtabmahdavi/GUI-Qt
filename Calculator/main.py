from math import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from functools import partial


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("calculator.ui")
        self.ui.show()

        self.ui.btn_0.clicked.connect(partial(self.show_number, "0"))
        self.ui.btn_1.clicked.connect(partial(self.show_number, "1"))
        self.ui.btn_2.clicked.connect(partial(self.show_number, "2"))
        self.ui.btn_3.clicked.connect(partial(self.show_number, "3"))
        self.ui.btn_4.clicked.connect(partial(self.show_number, "4"))
        self.ui.btn_5.clicked.connect(partial(self.show_number, "5"))
        self.ui.btn_6.clicked.connect(partial(self.show_number, "6"))
        self.ui.btn_7.clicked.connect(partial(self.show_number, "7"))
        self.ui.btn_8.clicked.connect(partial(self.show_number, "8"))
        self.ui.btn_9.clicked.connect(partial(self.show_number, "9"))
        self.ui.btn_dot.clicked.connect(partial(self.show_number, "."))
        self.ui.btn_negative.clicked.connect(partial(self.show_symbol, "-"))
        self.ui.btn_percent.clicked.connect(partial(self.show_symbol, "%"))

        self.ui.btn_sum.clicked.connect(partial(self.calculate, "sum"))
        self.ui.btn_subtract.clicked.connect(partial(self.calculate, "subtract"))
        self.ui.btn_multiply.clicked.connect(partial(self.calculate, "multiply"))
        self.ui.btn_divide.clicked.connect(partial(self.calculate, "divide"))
        self.ui.btn_power.clicked.connect(partial(self.calculate, "power"))
        self.ui.btn_square_root.clicked.connect(partial(self.calculate, "square root"))

        self.ui.btn_sin.clicked.connect(partial(self.show_symbol, "sin"))
        self.ui.btn_cos.clicked.connect(partial(self.show_symbol, "cos"))
        self.ui.btn_tan.clicked.connect(partial(self.show_symbol, "tan"))
        self.ui.btn_cot.clicked.connect(partial(self.show_symbol, "cot"))
        self.ui.btn_log.clicked.connect(partial(self.show_symbol, "log"))
        self.ui.btn_mod.clicked.connect(partial(self.show_symbol, "mod"))
        
        self.ui.btn_ac.clicked.connect(self.reset)
        self.ui.btn_equal.clicked.connect(self.equal)

    def show_number(self, number):
        self.ui.input_text.setText(self.ui.input_text.text() + number)

    def show_symbol(self, symbol):
        self.mode = symbol
        self.num1 = float(self.ui.input_text.text())
        self.ui.input_text.setText(symbol)

    def calculate(self, symbol):
        self.mode = symbol
        self.num1 = float(self.ui.input_text.text())
        self.ui.input_text.setText("")

    def equal(self):
        if self.mode == "sum":
            self.num2 = float(self.ui.input_text.text())
            result = self.num1 + self.num2
        elif self.mode == "subtract":
            self.num2 = float(self.ui.input_text.text())
            result = self.num1 - self.num2
        elif self.mode == "multiply":
            self.num2 = float(self.ui.input_text.text())
            result = self.num1 * self.num2
        elif self.mode == "divide":
            self.num2 = float(self.ui.input_text.text())
            if self.num2 != 0:
                result = self.num1 / self.num2
            else:
                result = "ERROR"
        elif self.mode == "power":
            self.num2 = float(self.ui.input_text.text())
            result = self.num1 ** self.num2
        elif self.mode == "square root":
            result = sqrt(self.num1)
        elif self.mode == "sin":
            result = sin(radians(self.num1))
        elif self.mode == "cos":
            result = cos(radians(self.num1))
        elif self.mode == "tan":
            result = tan(radians(self.num1))
        elif self.mode == "cot":
            result = 1 / tan(radians(self.num1))
        elif self.mode == "log":
            result = log10(self.num1)
        elif self.mode == "mod":
            self.num2 = float(self.ui.input_text
.text())
            result = self.num1 % self.num2
        self.ui.input_text.setText(str(result))

    def reset(self):
        self.ui.input_text.setText("")
        

if __name__ == "__main__":
    my_app = QApplication()
    main_window = Calculator()
    my_app.exec()