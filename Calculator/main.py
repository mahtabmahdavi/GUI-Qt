from math import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from functools import partial


class Calculator(QMainWindow):
    def __init__(self):
        # Properties
        super().__init__()
        self.num = ""

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

        self.ui.btn_pi.clicked.connect(partial(self.show_number, f"{pi}"))
        self.ui.btn_open.clicked.connect(partial(self.show_number, "("))
        self.ui.btn_closed.clicked.connect(partial(self.show_number, ")"))
        self.ui.btn_dot.clicked.connect(partial(self.show_number, "."))
        self.ui.btn_negative.clicked.connect(partial(self.show_symbol, "-", "neg"))
        self.ui.btn_percent.clicked.connect(partial(self.show_symbol, "%", "pct"))
        
        self.ui.btn_sum.clicked.connect(partial(self.show_symbol, "+", "sum"))
        self.ui.btn_subtract.clicked.connect(partial(self.show_symbol, "-", "sub"))
        self.ui.btn_multiply.clicked.connect(partial(self.show_symbol, "×", "mul"))
        self.ui.btn_divide.clicked.connect(partial(self.show_symbol, "÷", "div"))
        self.ui.btn_power.clicked.connect(partial(self.show_symbol, "^", "pow"))
        self.ui.btn_square_root.clicked.connect(partial(self.show_symbol, "√", "sqrt"))
        self.ui.btn_sin.clicked.connect(partial(self.show_symbol, "sin", "sin"))
        self.ui.btn_cos.clicked.connect(partial(self.show_symbol, "cos", "cos"))
        self.ui.btn_tan.clicked.connect(partial(self.show_symbol, "tan", "tan"))
        self.ui.btn_cot.clicked.connect(partial(self.show_symbol, "cot", "cot"))
        self.ui.btn_log.clicked.connect(partial(self.show_symbol, "log", "log"))
        self.ui.btn_mod.clicked.connect(partial(self.show_symbol, "mod", "mod"))
        
        self.ui.btn_ac.clicked.connect(self.reset)
        self.ui.btn_equal.clicked.connect(self.equal)

    # Methods
    def show_number(self, number):
        self.num += number
        self.ui.input_text.setText(self.ui.input_text.text() + number)
        
    def show_symbol(self, symbol, mode):
        self.mode = mode
        if self.mode == "sin" or self.mode == "cos" or self.mode == "tan" or self.mode == "cot" or self.mode == "log":
            self.ui.input_text.setText(self.ui.input_text.text() + symbol + " ")
        else:
            self.ui.input_text.setText(self.ui.input_text.text() + symbol)

    def calculate(self):
        if self.mode == "pct":
            self.expression = self.expression.split("%")
            return float(self.expression[0]) * 0.01
        elif self.mode == "sqrt":
            if self.num >= 0:
                return sqrt(float(self.num))
            else:
                return "ERROR"
        elif self.mode == "sin":
            return sin(radians(float(self.num)))
        elif self.mode == "cos":
            return cos(radians(float(self.num)))
        elif self.mode == "tan":
            return tan(radians(float(self.num)))
        elif self.mode == "cot":
            return 1 / tan(radians(float(self.num)))
        elif self.mode == "log":
            return log10(float(self.num))
        else:
            try:
                return float(eval(self.expression))
            except:
                return "ERROR"

    def equal(self):
        self.output = self.ui.input_text.text()
        self.expression = self.output

        if "×" in self.expression:
            self.expression = self.expression.replace("×", "*")
        if "÷" in self.expression:
            self.expression = self.expression.replace("÷", "/")
        if "^" in self.expression:
            self.expression = self.expression.replace("^", "**")
        if "mod" in self.expression:
            self.expression = self.expression.replace("mod", "%")
            
        result = str(self.calculate())
        self.output += ("=" + result)
        self.ui.input_text.setText(result)
        self.ui.output_text.setText(f"  {self.ui.output_text.text()}\n  {self.output}")
    
    def reset(self):
        self.num = ""
        self.ui.input_text.setText("")
        
# ----- End of Calculator class and its methods ----- #

if __name__ == "__main__":
    app = QApplication()
    main_window = Calculator()
    app.exec()