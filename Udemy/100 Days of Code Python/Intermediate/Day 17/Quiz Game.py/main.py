from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    q1 = item['text']
    a1 = item['answer']
    new_question = Question(q1, a1)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_qustions():
    print(quiz.still_has_qustions())
    quiz.next_question()
    




