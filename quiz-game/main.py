from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank:list = [Question(question['question'],question['correct_answer']) for question in question_data]
my_quiz_brain = QuizBrain(question_bank)

while my_quiz_brain.still_has_questions():
    my_quiz_brain.next_question()

print(f"You've completed the quiz!\nYour final score was: {my_quiz_brain.score}/{my_quiz_brain.question_number}")