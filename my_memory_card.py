#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 

questions_list.append(Question('what Epic the musical saga has the song god games?','wisdom saga', 'thunder saga', 'vengence saga', 'troy saga'))
questions_list.append(Question('what is the shortest song in Epic the musical?', "we'll be fine", 'i cant help but wonder', 'just a man', 'no longer you'))
questions_list.append(Question('how many times did the wind bag get opened in Epic the musical?', "3", '4', '5', '1'))
questions_list.append(Question('what inspired jorge riverra herans to write dangerous in Epic the musical?', "lights", 'a bird', 'another song', 'he just think of it randomly'))
questions_list.append(Question('how many songs are in Epic the musical?', "40", '43', '30', '45'))
questions_list.append(Question('how many sagas are in Epic the musical?', "9", '5', '7', '6'))
questions_list.append(Question('who is odysseus in Epic the musical?', "all of the above", 'nobody', 'the raining king of ithaca', 'a monster'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Quizz')

btn_OK = QPushButton('Answer')
lb_Question = QLabel('what is the most dangerous animal in the world?')

RadioGroupBox = QGroupBox("Answer options")

window.setStyleSheet("""
QWidget {
    background-color: #691616;
    color: white;
    font-family: Segoe UI;
    font-size: 14px;
}

QGroupBox {
    border: 2px solid #bf3232;
    border-radius: 15px;
    margin-top: 10px;
    padding: 15px;
    background-color: #691616;
    font-weight: bold;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 5px 0 5px;
    color: #e07979;
}

QLabel {
    font-size: 16px;
}

QRadioButton {
    spacing: 10px;
    padding: 8px;
}

QRadioButton::indicator {
    width: 18px;
    height: 18px;
}

QRadioButton::indicator:unchecked {
    border: 2px solid #e07979;
    border-radius: 9px;
    background: transparent;
}

QRadioButton::indicator:checked {
    background-color: #e07979;
    border: 2px solid #e07979;
    border-radius: 9px;
}

QPushButton {
    background-color: #e07979;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 15px;
    font-weight: bold;
    color: white;
}

QPushButton:hover {
    background-color: #e07979;
}

QPushButton:pressed {
    background-color: #e07979;
}
""")

rbtn_1 = QRadioButton('Lion')
rbtn_2 = QRadioButton('Shark')
rbtn_3 = QRadioButton('Duck')
rbtn_4 = QRadioButton('Rat')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?')
lb_Correct = QLabel('the answer will be here!')

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # the vertical ones will be inside the horizontal ones
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test results
layout_line3 = QHBoxLayout() # "Answer" button

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # the button should be large
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between the content
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')

    RadioGroup.setExclusive(False) # remove limits in order to reset radio button selection
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)   
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

from random import shuffle

def ask(q: Question):
    shuffle(answers)
    answers[ 0 ].setText(q.right_answer)
    answers[ 1 ].setText(q.wrong1)
    answers[ 2 ].setText(q.wrong2)
    answers[ 3 ].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Correct')
        window.score += 1
        print('Statistics\n-Total questions:',window.total,'\n- Right answers:', window.score)
        print('Rating:',(window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct( 'Incorrect' )
            print('Rating:',(window.score/window.total*100),'%')

from random import randint

def next_question():
    ''' Asks the next question in the list. '''
    # this function needs a variable that gives the number of the current question 
    # this variable can be made global, or it can be the property of a "global object" (app or window)
    # we will create the property window.cur_question (below)
    window.total += 1 # move on to the next question
    print('Statistics\n-Total questions:',window.total,'\n- Right answers:', window.score)
    cur_question = randint(0, len(questions_list)-1) 
    if cur_question >= len(questions_list):
        cur_question = 0 # if the list of questions has ended, start over 
    q = questions_list[cur_question] # take a question
    ask(q) # ask it

def click_OK():
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()

window.total = 0
window.score = 0

btn_OK.clicked.connect(click_OK)

next_question()

window.setLayout(layout_card)
window.show()
app.exec()
