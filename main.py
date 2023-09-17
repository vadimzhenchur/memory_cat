import random
from PyQt5.QtWidgets import *
import base
import TREBA
import editwindow
app = QApplication([])
app.setStyleSheet("""
     QWidget{
          background-color: #A0E7E5;
          }
     QPushButton{
        
        background-color: #BCECE0;
        border-width: 10px;
        border-color: #04ECF0;
        border-style: inset;
        font-family: Impact;
        min-width: 0em;
        padding: 10px;
        border-radius: 10px;
        
        }
     QGroupBox {
        border-style: inset;
        border-width: 10px;
        border-color: #059DC0;
        border-radius: 10px;
        font-family: Impact;
        }
     QSpinBox {
        border-style: inset;
        border-width: 10px;
        border-color: #15B5B0;
        border-radius: 10px;
        font-family: Impact;
        }
        QLabel {
        border-style: inset;
        border-width: 10px;
        max-height: 20px;
        man-width: 40px;
        border-color: #E7F2F8;
        border-radius: 10px;
        font-family: Impact;
        }
          """)

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
edit = QPushButton("Редагувати")
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
qwertyLine.addWidget(edit)
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

def nextFunc():
    answers[0].show()
    answers[1].show()
    answers[2].show()
    answers[3].show()
    Anwer.show()
    result.hide()
    base.currentQuest += 1
    setQuest()

def editQuestFunc():
    window.hide()
    editwindow.editwindow1()
    window.show()

    setQuest()

menuBth.clicked.connect(TREBA.menuWind)
edit.clicked.connect(editQuestFunc)
Anwer.clicked.connect(showResult)

Anwer2.clicked.connect(nextFunc)
window.setLayout(mainLine)
window.show()
app.exec()
