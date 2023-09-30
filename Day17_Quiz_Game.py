question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question:
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer



class QuizBrain:
    def __init__(self, li) -> None:
        self.question_number = 0
        self.questions_list = li
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.questions_list)
    
    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {question.text}", end = " ")
        answer = input("(True/False)?: ")

        self.check_answer(question, answer)
    
    def check_answer(self, question, answer):
        if answer.lower() == question.answer.lower():
            self.score += 1
            print("You got it right!")
        
        else: 
            print("You got it wrong.")

        print(f"The correct answer was: {question.answer}")
        print(f"Your score is: {self.score}/{self.question_number}.\n\n")
        
#https://opentdb.com/api_config.php take data from here and put in question_data
question_bank = [Question(data['question'], data['correct_answer']) for data in question_data]
quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")