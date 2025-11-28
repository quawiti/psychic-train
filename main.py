from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QGroupBox
class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3    
questions_list = []
questions_list.append(Question('Лучшая кличка для питомца', 'Титус', 'Бобик', 'Шарик', 'Тузик'))
questions_list.append(Question('Лучшая еда в мире', 'буузы', 'манты', 'хинкали', 'пельмени'))
questions_list.append(Question('Лучший урок в школе', 'обед', 'литература', 'русский', 'математика'))
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
question = QLabel('проверка')
answers = QGroupBox('Варианты ответов')
ans_btn = QPushButton('Ответить')
shuffle(questions_list)
ans1 = QRadioButton('1')
ans2 = QRadioButton('2')
ans3 = QRadioButton('3')
ans4 = QRadioButton('4')
radio_group = QButtonGroup()
radio_group.addButton(ans1)
radio_group.addButton(ans2)
radio_group.addButton(ans3)
radio_group.addButton(ans4)
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout2.addWidget(ans1)
layout2.addWidget(ans2)
layout3.addWidget(ans3)
layout3.addWidget(ans4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
answers.setLayout(layout1)
results = QGroupBox('Результаты теста')
decision = QLabel('Правильно/Неправильно')
correct = QLabel('Правильный ответ')
result_layout = QVBoxLayout()
result_layout.addWidget(decision, alignment= (Qt.AlignLeft|Qt.AlignTop))
result_layout.addWidget(correct, alignment= (Qt.AlignHCenter), stretch=2)
results.setLayout(result_layout)
results.hide()
main_layout1 = QHBoxLayout()
main_layout2 = QHBoxLayout()
main_layout3 = QHBoxLayout()
main_layout4 = QVBoxLayout()
main_layout1.addWidget(question, alignment=Qt.AlignCenter)
main_layout2.addWidget(results)
main_layout2.addWidget(answers)
main_layout3.addWidget(ans_btn, stretch=2)
main_layout4.addLayout(main_layout1)
main_layout4.addLayout(main_layout2)
main_layout4.addLayout(main_layout3)
main_layout4.setSpacing(5)
window.setLayout(main_layout4)
def show_result():
    answers.hide()
    results.show()
    ans_btn.setText('Следующий вопрос')
def show_question():
    results.hide()
    answers.show()
    ans_btn.setText('Ответить')
    radio_group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    radio_group.setExclusive(True)
# def test():
#     if ans_btn.text() == 'Ответить':
#         show_result()
#     else:
#         show_question()
# вас обманули это не physics-train, это psychic-train!!!!
answers_list = [ans1, ans2, ans3, ans4]
def ask(q: Question):
    shuffle(answers_list)
    answers_list[0].setText(q.right_answer)
    answers_list[1].setText(q.wrong1)
    answers_list[2].setText(q.wrong2)
    answers_list[3].setText(q.wrong3)
    question.setText(q.quest)
    correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    decision.setText(res)
    show_result()
def check_answer():
    if answers_list[0].isChecked():
        show_correct('Правильно')
        window.score += 1
    elif answers_list[1].isChecked() or answers_list[2].isChecked() or answers_list[3].isChecked():
        show_correct('Неверно')
def next_question():
    window.cur_question += 1
    if len(questions_list) <= window.cur_question:
        window.cur_question = 0
        print('Статистика\n- Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
        ans_btn.setText('Тест закончен')
    else:
        window.total += 1
        q = questions_list[window.cur_question]
        ask(q)
def click_ok():
    if ans_btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
window.cur_question = -1
ans_btn.clicked.connect(click_ok)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec_()
#создай приложение для запоминания информации
