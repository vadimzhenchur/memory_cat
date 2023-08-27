import random
from PyQt5.QtWidgets import *
import base

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
Anwer2 = QPushButton("Наступне питання")

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
answers = [answer1, answer2, answer3, answer4]


answerLine.addWidget(answer1)
answerLine.addWidget(answer2)
answerLine.addWidget(answer3)
answerLine.addWidget(answer4)
answerGroups.setLayout(answerLine)
mainLine.addWidget(answerGroups)

result = QLabel("Результат")
answerLine.addWidget(result)
result.hide()

qwertyLine = QHBoxLayout()
qwertyLine.addWidget(Anwer)
qwertyLine.addWidget(Anwer2)
mainLine.addLayout(qwertyLine)
Anwer2.hide()

def setQuest():
    random.shuffle(answers)
    Anwer1.setText(base.qeust[base.currentQuest]["питання"])
    answers[3].setText(base.qeust[base.currentQuest]["не правильна1"])
    answers[1].setText(base.qeust[base.currentQuest]["не правильна2"])
    answers[2].setText(base.qeust[base.currentQuest]["не правильна3"])
    answers[0].setText(base.qeust[base.currentQuest]["Правильна відповідь"])
setQuest()
def showResult():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    result.show()
    Anwer2.show()
    Anwer.hide()
    if answers[0].isChecked():
        result.setText("Правильно")
    else:
        result.setText("не правильно")



Anwer.clicked.connect(showResult)

window.setLayout(mainLine)
window.show()
app.exec()
