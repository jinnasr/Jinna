# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
  
import sys
  
  
class Window(QMainWindow):
        #
    def __init__(self):
        super().__init__()
  
        
        self.setWindowTitle("Calcu ")
  
        
        self.setGeometry(80, 80, 360, 350)
  
        
        self.UiComponents()
  
        
        self.show()
  
        #
    def UiComponents(self):
  
        
        self.label = QLabel(self)
  
        
        self.label.setGeometry(5, 5, 350, 70)
  
        
        self.label.setWordWrap(True)
  
        
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px whte;"
                                 "background : pink;"
                                 "}")
  
        
        self.label.setAlignment(Qt.AlignRight)
  
        
        self.label.setFont(QFont('Arial', 15))
  
  
        
        
        button1 = QPushButton("1", self)
  
        
        button1.setGeometry(5, 150, 80, 40)
  
        
        button2 = QPushButton("2", self)
  
       
        button2.setGeometry(95, 150, 80, 40)
  
        
        button3 = QPushButton("3", self)
  
        
        button3.setGeometry(185, 150, 80, 40)
  
        
        button4 = QPushButton("4", self)
  
        
        button4.setGeometry(5, 200, 80, 40)
  
        
        button5 = QPushButton("5", self)
  
        
        button5.setGeometry(95, 200, 80, 40)
  
        
        button6 = QPushButton("5", self)
  
        
        button6.setGeometry(185, 200, 80, 40)
  
        
        button7 = QPushButton("7", self)
  
        
        button7.setGeometry(5, 250, 80, 40)
  
        
        button8 = QPushButton("8", self)
  
        
        button8.setGeometry(95, 250, 80, 40)
  
        
        button9 = QPushButton("9", self)
  
        
        button9.setGeometry(185, 250, 80, 40)
  
        
        button0 = QPushButton("0", self)
  
        
        button0.setGeometry(5, 300, 80, 40)
  
        
        
        button_equal = QPushButton("=", self)
  
        
        button_equal.setGeometry(275, 300, 80, 40)
  
        
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        button_equal.setGraphicsEffect(c_effect)
  
        
        button_plus = QPushButton("+", self)
  
        
        button_plus.setGeometry(275, 250, 80, 40)
  
        
        button_minus = QPushButton("-", self)
  
        
        button_minus.setGeometry(275, 200, 80, 40)
  
        
        button_multiply = QPushButton("*", self)
  
        
        button_multiply.setGeometry(275, 150, 80, 40)
  
        
        button_divide = QPushButton("/", self)
  
        
        button_divide.setGeometry(185, 300, 80, 40)
  
        
        button_point = QPushButton(".", self)
  
        
        button_point.setGeometry(95, 300, 80, 40)
  
  
        
        button_clear = QPushButton("Clear", self)
        button_clear.setGeometry(5, 100, 200, 40)
  
        
        button_delete = QPushButton("Del", self)
        button_delete.setGeometry(210, 100, 145, 40)
  
        
        button_minus.clicked.connect(self.press_minus)
        button_equal.clicked.connect(self.press_equal)
        button0.clicked.connect(self.press0)
        button1.clicked.connect(self.press1)
        button2.clicked.connect(self.press2)
        button3.clicked.connect(self.press3)
        button4.clicked.connect(self.press4)
        button5.clicked.connect(self.press5)
        button6.clicked.connect(self.press6)
        button7.clicked.connect(self.press7)
        button8.clicked.connect(self.press8)
        button9.clicked.connect(self.press9)
        button_divide.clicked.connect(self.press_divide)
        button_multiply.clicked.connect(self.press_multiply)
        button_plus.clicked.connect(self.press_plus)
        button_point.clicked.connect(self.press_point)
        button_clear.clicked.connect(self.press_clear)
        button_delete.clicked.connect(self.press_delete)
  
        #
    def press_equal(self):
  
        
        equation = self.label.text()
  
        try:
            
            ans = eval(equation)
  
            
            self.label.setText(str(ans))
  
        except:
            
            self.label.setText("Wrong Input")
        #
    def press_plus(self):
        
        text = self.label.text()
        self.label.setText(text + " + ")
        #
    def press_minus(self):
        
        text = self.label.text()
        self.label.setText(text + " - ")
        #
    def press_divide(self):
        
        text = self.label.text()
        self.label.setText(text + " / ")
        #
    def press_multiply(self):
        
        text = self.label.text()
        self.label.setText(text + " * ")
        #
    def press_point(self):
       
        text = self.label.text()
        self.label.setText(text + ".")
        #
    def press0(self):
        
        text = self.label.text()
        self.label.setText(text + "0")
        #
    def press1(self):
        
        text = self.label.text()
        self.label.setText(text + "1")
        #
    def press2(self):
        
        text = self.label.text()
        self.label.setText(text + "2")
        #
    def press3(self):
        
        text = self.label.text()
        self.label.setText(text + "3")
        #
    def press4(self):
        
        text = self.label.text()
        self.label.setText(text + "4")
        #
    def press5(self):
       
        text = self.label.text()
        self.label.setText(text + "5")
        #
    def press6(self):
       
        text = self.label.text()
        self.label.setText(text + "6")
        #
    def press7(self):
        
        text = self.label.text()
        self.label.setText(text + "7")
        #
    def press8(self):
       
        text = self.label.text()
        self.label.setText(text + "8")
        #
    def press9(self):
       
        text = self.label.text()
        self.label.setText(text + "9")
        #
    def press_clear(self):
       
        self.label.setText("")
        #
    def press_delete(self):
        
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())