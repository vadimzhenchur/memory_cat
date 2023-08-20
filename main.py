from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

window.resize(500, 500)

mainLine = QVBoxLayout()

menuBth = QPushButton("Menu")
restBth = QPushButton("Відпочити")
timeSpn = QSpinBox()
timeLbl = QLabel("хвилин")
Anwer = QPushButton("Відповісти")
Anwer1 = QLabel("Яблуко")


firstLine = QHBoxLayout()
firstLine.addWidget(menuBth)
firstLine.addWidget(restBth)
firstLine.addWidget(timeSpn)
firstLine.addWidget(timeLbl)
mainLine.addLayout(firstLine)
qLine = QHBoxLayout()
qLine.addWidget(Anwer1)
mainLine.addLayout(qLine)


answerGroups = QGroupBox("Введи правильну відповідь!")
answerLine = QVBoxLayout()
answer1 = QRadioButton("1")
answer2 = QRadioButton("2")
answer3 = QRadioButton("3")
answer4 = QRadioButton("4")

answerLine.addWidget(answer1)
answerLine.addWidget(answer2)
answerLine.addWidget(answer3)
answerLine.addWidget(answer4)
answerGroups.setLayout(answerLine)
mainLine.addWidget(answerGroups)

qwertyLine = QHBoxLayout()
qwertyLine.addWidget(Anwer)
mainLine.addLayout(qwertyLine)

window.setLayout(mainLine)
window.show()
app.exec()
