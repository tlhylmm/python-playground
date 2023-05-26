from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dict in question_data:
     question_bank.append(Question(dict["text"], dict["answer"]))

new_quiz = QuizBrain(question_bank) 

while new_quiz.still_has_questions():
    new_quiz.next_question()
    print("\n")

print(f"You've completed the quiz!")
print(f"Your final score is {new_quiz.score}/{new_quiz.question_number}.")