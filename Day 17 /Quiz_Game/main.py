from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    question_text = entry["text"]
    question_answer = entry["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print('You have completed the quiz!')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')
