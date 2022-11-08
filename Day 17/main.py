from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.has_more_questions():
    quiz.next_question()

if quiz.score == len(question_bank):
    print(f"Congratulations!!!. It's a perfect score.")
else:
    print(f"Better luck next time. Your score was {quiz.score}/{len(question_bank)}")
