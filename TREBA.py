from PyQt5.QtWidgets import *

import base


def menuWind():
    window = QDialog()

    rightAnswerlbt = QLabel("Правильна відповідь")

    asdf = QLabel("Питання")
    asdf1 = QLabel("Правильна відповідь")
    asdf2 = QLabel("не правильна1")
    asdf3 = QLabel("не правльна2")
    asdf4 = QLabel("не правильна3")
    fdsa = QLineEdit()
    fdsa1 = QLineEdit()
    fdsa2 = QLineEdit()
    fdsa3 = QLineEdit()
    fdsa4 = QLineEdit()

    addBth = QPushButton("Добавити")


    mainLine = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(asdf)
    h1.addWidget(fdsa)
    mainLine.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(asdf1)
    h2.addWidget(fdsa1)
    mainLine.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(asdf2)
    h3.addWidget(fdsa2)
    mainLine.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(asdf3)
    h4.addWidget(fdsa3)
    mainLine.addLayout(h4)

    h5 = QHBoxLayout()
    h5.addWidget(asdf4)
    h5.addWidget(fdsa4)
    mainLine.addLayout(h5)

    h6 = QHBoxLayout()
    h6.addWidget(rightAnswerlbt)

    mainLine.addLayout(h6)

    h7 = QHBoxLayout()
    h7.addWidget(addBth)

    mainLine.addLayout(h7)





import base


def menuWind():
    window = QDialog()

    rightAnswerlbt = QLabel("Правильна відповідь")

    asdf = QLabel("Питання")
    asdf1 = QLabel("Правильна відповідь")
    asdf2 = QLabel("не правильна1")
    asdf3 = QLabel("не правльна2")
    asdf4 = QLabel("не правильна3")
    fdsa = QLineEdit()
    fdsa1 = QLineEdit()
    fdsa2 = QLineEdit()
    fdsa3 = QLineEdit()
    fdsa4 = QLineEdit()

    addBth = QPushButton("Добавити")


    mainLine = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(asdf)
    h1.addWidget(fdsa)
    mainLine.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(asdf1)
    h2.addWidget(fdsa1)
    mainLine.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(asdf2)
    h3.addWidget(fdsa2)
    mainLine.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(asdf3)
    h4.addWidget(fdsa3)
    mainLine.addLayout(h4)

    h5 = QHBoxLayout()
    h5.addWidget(asdf4)
    h5.addWidget(fdsa4)
    mainLine.addLayout(h5)

    h6 = QHBoxLayout()
    h6.addWidget(rightAnswerlbt)

    mainLine.addLayout(h6)

    h7 = QHBoxLayout()
    h7.addWidget(addBth)

    mainLine.addLayout(h7)

    def addFunc():
        base.qeust.append(
            {
                "питання": fdsa.text(),
                "Правильна відповідь": fdsa1.text(),
                "не правильна1": fdsa2.text(),
                "не правильна2": fdsa3.text(),
                "не правильна3": fdsa.text()
            }
        )

    mainLine.addWidget(addBth)
    addBth.clicked.connect(addFunc)
    window.setLayout(mainLine)
    window.show()
    window.exec()



    mainLine.addWidget(addBth)
    addBth.clicked.connect(addFunc)
    window.setLayout(mainLine)
    window.show()
    window.exec()
