import sys
from functools import partial

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget, QHBoxLayout,
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        self.setMinimumSize(QSize(300,300))

        layout = QVBoxLayout()

        global label
        label = QLabel()
        layout.addWidget(label)
        font = QFont()
        font.setPointSize(20)
        label.setFont(font)

        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()

        for i in range(0,3):
            buttonNum = QPushButton(str(i+1))
            layout1.addWidget(buttonNum)
            buttonNum.clicked.connect(partial(self.numClicked, i+1))

        buttonChar = QPushButton("+")
        layout1.addWidget(buttonChar)
        buttonChar.clicked.connect(partial(self.charClicked, "+"))

        for i in range(3,6):
            buttonNum = QPushButton(str(i+1))
            layout2.addWidget(buttonNum)
            buttonNum.clicked.connect(partial(self.numClicked, i+1))

        buttonChar = QPushButton("-")
        layout2.addWidget(buttonChar)
        buttonChar.clicked.connect(partial(self.charClicked, "-"))

        for i in range(6,9):
            buttonNum = QPushButton(str(i+1))
            layout3.addWidget(buttonNum)
            buttonNum.clicked.connect(partial(self.numClicked, i+1))

        buttonChar = QPushButton("*")
        layout3.addWidget(buttonChar)
        buttonChar.clicked.connect(partial(self.charClicked, "*"))


        buttonNum = QPushButton('0')
        layout4.addWidget(buttonNum)
        buttonNum.clicked.connect(partial(self.numClicked, 0))

        buttonChar = QPushButton(".")
        layout4.addWidget(buttonChar)
        buttonChar.clicked.connect(partial(self.charClicked, "."))

        buttonChar = QPushButton("=")
        layout4.addWidget(buttonChar)
        buttonChar.clicked.connect(partial(self.charClicked, "="))

        buttonChar = QPushButton("/")
        layout4.addWidget(buttonChar)
        buttonChar.clicked.connect(partial(self.charClicked, "/"))

        buttonChar = QPushButton("C")
        layout5.addWidget(buttonChar)
        buttonChar.clicked.connect(partial(self.charClicked, "C"))

        buttonChar = QPushButton("CA")
        layout5.addWidget(buttonChar)
        buttonChar.clicked.connect(partial(self.charClicked, "CA"))


        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)
        layout.addLayout(layout5)

        #- + * / =
        global char_arr
        char_arr = ['+', '-', '*', '/', '=', 'C', 'CA','.']

        # for c in char_arr:
        #     buttonChar = QPushButton(c)
        #     layout.addWidget(buttonChar)
        #     buttonChar.clicked.connect(partial(self.charClicked, c))

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def numClicked(self, num):
        temp = label.text()
        if(temp):
            if (temp[len(temp) - 1] != "/" or num != 0):
                label.setText(temp + str(num))
            else:
                print("cannot do next operation")
        else:
            if (num != 0):
                label.setText(temp + str(num))
            else:
                print("cannot do next operation")

    def charClicked(self, c):
        temp = label.text()
        if(temp != ""):
            if (c == 'CA'):
                label.setText("")
            elif (c == "C"):
                temp = temp[:-1]
                label.setText(temp)
            else:
                last = temp[len(temp) - 1]
                if last in char_arr:
                    print("cannot do next operation")
                else:
                    if (c == "="):
                        res = eval(temp)
                        res = round(res, 2)
                        label.setText(str(res))
                    elif (c == "."):
                        temp2 = temp + c
                        try:
                            eval(temp2)
                            label.setText(temp + c)
                        except:
                            print("cannot do next operation")
                    else:
                        label.setText(temp + c)
        else:
            print("cannot do next operation")




app = QApplication()
window = MainWindow()
window.show()
app.exec()