from PyQt5.QtWidgets import *

import base

def editwindow1():
    window = QDialog()



    asdf = QLabel("Питання")
    asdf1 = QLabel("Правильна відповідь")
    asdf2 = QLabel("не правильна1")
    asdf3 = QLabel("не правльна2")
    asdf4 = QLabel("не правильна3")
    fdsa = QLineEdit()
    fdsa.setText(base.qeust[base.currentQuest]["питання"])
    fdsa1 = QLineEdit()
    fdsa1.setText(base.qeust[base.currentQuest]["Правильна відповідь"])
    fdsa2 = QLineEdit()
    fdsa2.setText(base.qeust[base.currentQuest]["не правильна1"])
    fdsa3 = QLineEdit()
    fdsa3.setText(base.qeust[base.currentQuest]["не правильна2"])
    fdsa4 = QLineEdit()
    fdsa4.setText(base.qeust[base.currentQuest]["не правильна3"])

    addBth = QPushButton("Добавити")

    mainLine = QVBoxLayout()
    def Treba():
        base.qeust[base.currentQuest] = (
            {
                "питання": fdsa.text(),
                "Правильна відповідь": fdsa1.text(),
                "не правильна1": fdsa2.text(),
                "не правильна2": fdsa3.text(),
                "не правильна3": fdsa.text()
            }
        )
    mainLine.addWidget(asdf)
    mainLine.addWidget(fdsa)
    mainLine.addWidget(asdf1)
    mainLine.addWidget(fdsa1)

    mainLine.addWidget(asdf2)
    mainLine.addWidget(fdsa2)
    mainLine.addWidget(asdf3)
    mainLine.addWidget(fdsa3)
    mainLine.addWidget(asdf4)
    mainLine.addWidget(fdsa4)
    mainLine.addWidget(addBth)
    addBth.clicked.connect(Treba)
    window.setLayout(mainLine)
    window.show()
    window.exec()
